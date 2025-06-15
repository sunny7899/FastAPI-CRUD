from sqlmodel import Session
from models import Item
from database import engine
from fastapi.middleware.cors import CORSMiddleware
item = Item(id=1, owner_id="auth0|user-id-from-token", data="Secret data")

with Session(engine) as session:
    session.add(item)
    session.commit()
