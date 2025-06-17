Set up a model-specific permissions function for a FastAPI CRUD endpoint that allows users who own the model instance to read the object, and also an auth0 m2m app to read the object.

├── main.py
├── auth.py
├── models.py
├── database.py
├── crud.py
├── routers/
│   └── resource.py
├── requirements.txt
└── .env

http://127.0.0.1:8000/
http://127.0.0.1:8000/docs

https://manage.auth0.com/

https://jwt.io/


{
  "alg": "RS256",
  "typ": "JWT",
  "kid": "abc123xyz"
}
access token
{
  "alg": "dir",
  "enc": "A256GCM",
  "iss": "https://dev-swp17yxdc7p6unqh.us.auth0.com/"
}

Decoded Header
{
  "alg": "RS256",
  "typ": "JWT",
  "kid": "RtmCxLDXoS6N04YlrggA3"
}

id token 
{
  "alg": "RS256",
  "typ": "JWT",
  "kid": "RtmCxLDXoS6N04YlrggA3"
}

Decoded Payload
{
  "iss": "https://dev-swp17yxdc7p6unqh.us.auth0.com/",
  "sub": "google-oauth2|100412700466377214282",
  "aud": [
    "https://fastapi.example.com",
    "https://dev-swp17yxdc7p6unqh.us.auth0.com/userinfo"
  ],
  "iat": 1749919935,
  "exp": 1750006335,
  "scope": "openid profile email",
  "azp": "WP06JJjDmYruqp51NtlEriD7P7xwGw3z",
  "permissions": []
}

# load_dotenv
# Auth0 OAuth2 Scheme
# Database Setup
# Fetch Auth0's JWKS (JSON Web Key Set)
# Verify Auth0 token
# Permissions function
# Homepage
# Routes - login, logout, callback

1. python -m venv venv
.\venv\Scripts\activate
It prevents package version conflicts between projects.
Makes projects more portable and reproducible.
Keeps your system Python installation clean.
Allows testing with different Python versions.

2. uvicorn main:app --reload


{
  "access_token": "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIiwiaXNzIjoiaHR0cHM6Ly9kZXYtc3dwMTd5eGRjN3A2dW5xaC51cy5hdXRoMC5jb20vIn0..JzhMzRlBTkKLU-1a.mAHQJWxvK8-_gk0TUkHMDe6od7QbCSCWt1lSdQZzjyE8ZuakdRUv8yxGfwW8W8709NRzn2-0SSwTmjk1kcfdlhcoVP4R39dxT7xqiV99gXpFixsCN4OloO3A4AF7uKZBl0p8unbzyqi1XhPMvYGex5fm4Szd1tNvT5kU-lwf2IFigV4ZclZ9Atve6Shv1PgpfxC-XIunyABlEU1caOfN6TYvEgMRWT8NzhCP5vIPQQYrc8MDRRJrLFC2dLeHlI4mKF9AaBGXNoJ29xulaH1VtwdlGBlDE7lG-yGrYjQ_nlhnu0OkxUX97OIIMM1vRwQkc3h7oyfYRWclOPUw5U3XFvXMq12L_PQ.XVqWFdBDAJk0VxP9vktzgQ",
  "id_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJ0bUN4TERYb1M2TjA0WWxyZ2dBMyJ9.eyJnaXZlbl9uYW1lIjoic3VubnkiLCJmYW1pbHlfbmFtZSI6Imd1cHRhIiwibmlja25hbWUiOiJzdW5ueWd1cHRhLnNoaXZhbSIsIm5hbWUiOiJzdW5ueSBndXB0YSIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BQ2c4b2NJa0hMbFRKUjY3Rkdxckl1dnZYeDIxcm5uWURjTG5Ueml0Q2tKN09QeVJUZGs0Wmx6Yz1zOTYtYyIsInVwZGF0ZWRfYXQiOiIyMDI1LTA2LTEyVDA1OjM0OjMxLjA5M1oiLCJlbWFpbCI6InN1bm55Z3VwdGEuc2hpdmFtQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJpc3MiOiJodHRwczovL2Rldi1zd3AxN3l4ZGM3cDZ1bnFoLnVzLmF1dGgwLmNvbS8iLCJhdWQiOiJXUDA2SkpqRG1ZcnVxcDUxTnRsRXJpRDdQN3h3R3czeiIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTAwNDEyNzAwNDY2Mzc3MjE0MjgyIiwiaWF0IjoxNzQ5NzA2NDgyLCJleHAiOjE3NDk3NDI0ODIsInNpZCI6IlhlMXVVM01xbC1WdGRZUDNoLUJIOE9PanZ5WThFMUUtIn0.RF3aow3L_o3mWUHErkc146ZMrV1ovWK-BlA5ix1d04jRe5GNyw5zUOfgiztO0fkWqmtmc63Bts9LbdpploThjJjsmUqpDXEbzknEHBtaBbN7lbC0PnDPgpTvi9YkN3JfWd-xOsT4SI5wxs6TklbjMlO9i2OPf5J7s37nTZf8-VHrldlkvkPFO0R7cYskbhdPmivUR71ux24ni7UOzskobLzDW_Y5EhF5WpTvo2_Q3d4dbQiqsszAZlV4ubWpXmfy7Zxj3OpMptKGzf__fmnaKf5R9QBEaE0BQzGigNfBvlJHmmvSJmFBXSWjGIQfc24mvLUTgDRFxBEiNH0LjrdvHg",
  "scope": "openid profile email",
  "expires_in": 86400,
  "token_type": "Bearer"
}

curl.exe -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJ0bUN4TERYb1M2TjA0WWxyZ2dBMyJ9.eyJpc3MiOiJodHRwczovL2Rldi1zd3AxN3l4ZGM3cDZ1bnFoLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwMDQxMjcwMDQ2NjM3NzIxNDI4MiIsImF1ZCI6WyJodHRwczovL2Zhc3RhcGkuZXhhbXBsZS5jb20iLCJodHRwczovL2Rldi1zd3AxN3l4ZGM3cDZ1bnFoLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE3NDk5NjAyMjEsImV4cCI6MTc1MDA0NjYyMSwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsImF6cCI6IldQMDZKSmpEbVlydXFwNTFOdGxFcmlEN1A3eHdHdzN6IiwicGVybWlzc2lvbnMiOltdfQ.nPWs3eIDHZu_wJlA95Wnr_-RbxfDW2s6-XvYDlxc9c88YB46CQeCQnrm41uNWAoEVs9qrDgzZ_UZXUwOWp1oKKWOJxGqmyhiuqVhrpUOv-vT9hoOjDveX1jTmIPaSrUSHefbp5PoWNrY5ODCIeRuBLVu0xhvOhoT7qobubJjRfvCeXdpLT3e7_UN2ALVGQNtOFvOz4uhNe8-clz4UdyTddDbx4uG5YYiadqqObRsoXwHglUtUguJyIloeQf8CJNzZTH6nrzW30Sw-qI08yI76eU0VG4NI7xqV5QeTjGZyO6bHXNJGLEZ7kMzMSfEyuLAIBhRCX5bgzoxGVpvDeMAlA" http://127.0.0.1:8000/items/1


https://github.com/sunny7899/FastAPI-CRUD

pip install fastapi uvicorn python-dotenv requests jose[cryptography] sqlmodel 
pip3 install pipreqs

AUTH0_CLIENT_ID -> Application regular app
APIs domain is similar to base url Application
AUTH0_CLIENT_SECRET -> Application regular app
AUTH0_AUDIENCE -> APIs identifier Custom API
AUTH0_DOMAIN -> APIs base url

http://127.0.0.1:8000/callback  -> callback url

 it's likely used to allow access from a Machine-to-Machine (M2M) application instead of a human user.

 {
    "owner_id": "google-oauth2|100412700466377214282",
    "data": "Test data",
    "id": 2
}

allowed callback uris
http://127.0.0.1:8000/callback

http://127.0.0.1:8000/docs/oauth2-redirect



you should show the user who owns a model being able to access it and one who doesn't own it not having access
endpoint that allows users who own the model instance to read the object and an auth0 m2m app to read the object.