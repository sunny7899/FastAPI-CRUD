from fastapi import FastAPI, Depends, HTTPException, Security
from fastapi.security import OAuth2AuthorizationCodeBearer, HTTPBearer
from fastapi.responses import HTMLResponse, RedirectResponse
from jose import jwt, JWTError
from sqlmodel import SQLModel, Field, Session, create_engine, select
import requests
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from jose.backends.rsa_backend import RSAKey

# Load environment variables
load_dotenv()

AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")
AUTH0_CLIENT_ID = os.getenv("AUTH0_CLIENT_ID") #m2m client id
AUTH0_CLIENT_SECRET = os.getenv("AUTH0_CLIENT_SECRET")
AUTH0_AUDIENCE = os.getenv("AUTH0_AUDIENCE")
AUTH0_M2M_CLIENT_ID = os.getenv("AUTH0_M2M_CLIENT_ID")  # M2M client id
ALGORITHMS = ["RS256"]

# Auth0 OAuth2 Scheme
oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl=f"https://{AUTH0_DOMAIN}/authorize",
    tokenUrl=f"https://{AUTH0_DOMAIN}/oauth/token",
    scopes={"openid": "OpenID Connect scope"}
)

app = FastAPI(debug=True)
security = HTTPBearer()

# Database Setup
DATABASE_URL = "sqlite:///database.db"
engine = create_engine(DATABASE_URL)

class Item(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    owner_id: str #owner_id is mapped from the token’s sub claim.
    data: str

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

# Fetch Auth0's JWKS (JSON Web Key Set)
def get_jwks():
    jwks_url = f"https://{AUTH0_DOMAIN}/.well-known/jwks.json"
    try:
        response = requests.get(jwks_url)
        response.raise_for_status()
        return response.json()["keys"]
    except requests.RequestException:
        raise HTTPException(status_code=500, detail="Failed to fetch JWKS")

# Verify Auth0 token
def get_current_user(token: str = Security(oauth2_scheme)):
    if not token:
        raise HTTPException(status_code=401, detail="No access token provided")
    
    try:
        jwks = get_jwks()
        headers = jwt.get_unverified_header(token)
        kid = headers.get("kid")
        
        if not kid:
            raise HTTPException(status_code=401, detail="Invalid token: Missing KID")
        
        key = next((key for key in jwks if key["kid"] == kid), None)
        if not key:
            raise HTTPException(status_code=401, detail="Invalid token: Key not found")
        
        # public_key = jwt.algorithms.RSAAlgorithm.from_jwk(key)
        # public_key = RSAKey(key).to_pem().decode("utf-8")

        payload = jwt.decode(
            token,
            key=key,
            algorithms=ALGORITHMS,
            audience=AUTH0_AUDIENCE,
            issuer=f"https://{AUTH0_DOMAIN}/"
        )
        # print(f"Using public key: {public_key}", payload)
        return payload
    except JWTError as e:
        raise HTTPException(status_code=401, detail=f"Invalid token: {str(e)}")

# Permissions function
def get_item(item_id: int, user: dict):
    user_id = user["sub"]
    with Session(engine) as session:
        statement = select(Item).where(Item.id == item_id)
        item = session.exec(statement).first()
        print("Owner ID:", item.owner_id, is_m2m_user(user))

        if not item:
            raise HTTPException(status_code=404, detail="Item not found")
        if item.owner_id != user_id and not is_m2m_user(user):
            raise HTTPException(status_code=403, detail="Access denied")
        return item

# Homepage
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <body>
            <h2>Welcome to FastAPI Auth0 Integration</h2>
            <a href="/login">Login</a>  | <a href="/logout">Logout</a>
        </body>
    </html>
    """

@app.get("/analytics")
def get_analytics(user: dict = Depends(get_current_user)):
    if not is_m2m_user(user):
        raise HTTPException(status_code=403, detail="Only M2M apps allowed")
    return {"stats": "here's your analytics"}

# Routes
@app.get("/login")
def login():
    return RedirectResponse(
        url=f"https://{AUTH0_DOMAIN}/authorize?response_type=code&client_id={AUTH0_CLIENT_ID}&redirect_uri=http://127.0.0.1:8000/callback&scope=openid profile email&audience={AUTH0_AUDIENCE}"

    )

@app.get("/logout")
def logout():
    return RedirectResponse(
        url=f"https://{AUTH0_DOMAIN}/v2/logout?returnTo=http://127.0.0.1:8000&client_id={AUTH0_CLIENT_ID}"
    )

@app.get("/items", tags=["Dev"])
def list_all_items():
    with Session(engine) as session:
        items = session.exec(select(Item)).all()
        return items

@app.post("/add-item")
def add_item(user: dict = Depends(get_current_user)):
    print("sub:", user.get("sub"))
    print("azp:", user.get("azp"), is_m2m_user(user))
    with Session(engine) as session:
        new_item = Item(owner_id=user["sub"], data="Test dummy data")
        session.add(new_item)
        session.commit()
        session.refresh(new_item)
        return new_item

# m2m app token
@app.get("/callback")
def callback(code: str):
    token_url = f"https://{AUTH0_DOMAIN}/oauth/token"
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    data = {
        'grant_type': 'authorization_code',
        'client_id': AUTH0_CLIENT_ID,
        'client_secret': AUTH0_CLIENT_SECRET,
        'code': code,
        'redirect_uri': 'http://127.0.0.1:8000/callback'
    }
    response = requests.post(token_url, headers=headers, data=data)
    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Failed to retrieve access token")
    tokens = response.json()
    return tokens

# Protected Route - Requires Auth
@app.get("/connect-third-party")
def connect_third_party(user: dict = Depends(get_current_user)):
    third_party_data = {"data": "Synced successfully with third-party!"}
    return {"user": user, "third_party_data": third_party_data}

# Secure CRUD API for User Items items/{item_id} route that checks for ownership
@app.get("/items/{item_id}")
def read_item(item_id: int, user: dict = Depends(get_current_user)):
    return get_item(item_id, user)

@app.get("/test")
def test_endpoint():
    return {"message": "Test successful"}

def is_m2m_user(user: dict) -> bool:
    """
    Check if the token is from an M2M app (via azp/client_id).
    """
    return user.get("azp") == AUTH0_M2M_CLIENT_ID



# Secure M2M API for
