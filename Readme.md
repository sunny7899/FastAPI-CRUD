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
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJ0bUN4TERYb1M2TjA0WWxyZ2dBMyJ9.eyJpc3MiOiJodHRwczovL2Rldi1zd3AxN3l4ZGM3cDZ1bnFoLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwMDQxMjcwMDQ2NjM3NzIxNDI4MiIsImF1ZCI6WyJodHRwczovL2Zhc3RhcGkuZXhhbXBsZS5jb20iLCJodHRwczovL2Rldi1zd3AxN3l4ZGM3cDZ1bnFoLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE3NTAzMTkzNjIsImV4cCI6MTc1MDQwNTc2Miwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsImF6cCI6IldQMDZKSmpEbVlydXFwNTFOdGxFcmlEN1A3eHdHdzN6IiwicGVybWlzc2lvbnMiOltdfQ.jqtKS-NVXvIaUnPXY5ziQR_eWqm1E1IYiPlKw4Tn5IZnQqcCjYNIyWxk0gWa-D2TnPZ2SQuQReIF55j7uprXQgGwYoVFxCyh_Apr1y2wzFcRll0TMVsxMijjqz-Cy_RZXbvxqF7cHdVk-TVhO2O28Tnrrg_OIkLo_DbdkuRG2Jzj-B7P8w7FtB3FWamfWjVR136i1v9YRm3o3HI34Zv1-di_f-2bkYkug_Fv5gn67X95c7F1za753OdEGg4kIkqsKylAOxxFujAnLQnZwUPf0jmG8OXeAKtwmXu6rhMxeKoENrRx2hpCyT-5Ud5ZK0tsfQyfrs2mxlFwY3RMKJFn2Q",
  "id_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJ0bUN4TERYb1M2TjA0WWxyZ2dBMyJ9.eyJnaXZlbl9uYW1lIjoic3VubnkiLCJmYW1pbHlfbmFtZSI6Imd1cHRhIiwibmlja25hbWUiOiJzdW5ueWd1cHRhLnNoaXZhbSIsIm5hbWUiOiJzdW5ueSBndXB0YSIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BQ2c4b2NJa0hMbFRKUjY3Rkdxckl1dnZYeDIxcm5uWURjTG5Ueml0Q2tKN09QeVJUZGs0Wmx6Yz1zOTYtYyIsInVwZGF0ZWRfYXQiOiIyMDI1LTA2LTEyVDA1OjM0OjMxLjA5M1oiLCJlbWFpbCI6InN1bm55Z3VwdGEuc2hpdmFtQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJpc3MiOiJodHRwczovL2Rldi1zd3AxN3l4ZGM3cDZ1bnFoLnVzLmF1dGgwLmNvbS8iLCJhdWQiOiJXUDA2SkpqRG1ZcnVxcDUxTnRsRXJpRDdQN3h3R3czeiIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTAwNDEyNzAwNDY2Mzc3MjE0MjgyIiwiaWF0IjoxNzQ5NzA2NDgyLCJleHAiOjE3NDk3NDI0ODIsInNpZCI6IlhlMXVVM01xbC1WdGRZUDNoLUJIOE9PanZ5WThFMUUtIn0.RF3aow3L_o3mWUHErkc146ZMrV1ovWK-BlA5ix1d04jRe5GNyw5zUOfgiztO0fkWqmtmc63Bts9LbdpploThjJjsmUqpDXEbzknEHBtaBbN7lbC0PnDPgpTvi9YkN3JfWd-xOsT4SI5wxs6TklbjMlO9i2OPf5J7s37nTZf8-VHrldlkvkPFO0R7cYskbhdPmivUR71ux24ni7UOzskobLzDW_Y5EhF5WpTvo2_Q3d4dbQiqsszAZlV4ubWpXmfy7Zxj3OpMptKGzf__fmnaKf5R9QBEaE0BQzGigNfBvlJHmmvSJmFBXSWjGIQfc24mvLUTgDRFxBEiNH0LjrdvHg",
  "scope": "openid profile email",
  "expires_in": 86400,
  "token_type": "Bearer"
}

curl.exe -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJ0bUN4TERYb1M2TjA0WWxyZ2dBMyJ9.eyJpc3MiOiJodHRwczovL2Rldi1zd3AxN3l4ZGM3cDZ1bnFoLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwMDQxMjcwMDQ2NjM3NzIxNDI4MiIsImF1ZCI6WyJodHRwczovL2Zhc3RhcGkuZXhhbXBsZS5jb20iLCJodHRwczovL2Rldi1zd3AxN3l4ZGM3cDZ1bnFoLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE3NTAzMTkzNjIsImV4cCI6MTc1MDQwNTc2Miwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsImF6cCI6IldQMDZKSmpEbVlydXFwNTFOdGxFcmlEN1A3eHdHdzN6IiwicGVybWlzc2lvbnMiOltdfQ.jqtKS-NVXvIaUnPXY5ziQR_eWqm1E1IYiPlKw4Tn5IZnQqcCjYNIyWxk0gWa-D2TnPZ2SQuQReIF55j7uprXQgGwYoVFxCyh_Apr1y2wzFcRll0TMVsxMijjqz-Cy_RZXbvxqF7cHdVk-TVhO2O28Tnrrg_OIkLo_DbdkuRG2Jzj-B7P8w7FtB3FWamfWjVR136i1v9YRm3o3HI34Zv1-di_f-2bkYkug_Fv5gn67X95c7F1za753OdEGg4kIkqsKylAOxxFujAnLQnZwUPf0jmG8OXeAKtwmXu6rhMxeKoENrRx2hpCyT-5Ud5ZK0tsfQyfrs2mxlFwY3RMKJFn2Q" http://127.0.0.1:8000/items/1

curl.exe --request POST \
  --url https://dev-swp17yxdc7p6unqh.us.auth0.com/oauth/token \
  --header 'content-type: application/json' \
  --data '{
    "client_id":"B3ON51o8uuibtualLNIqogcdEq9qBCyF",
    "client_secret":"DahLvx1QbK9oJLuiWgexIRu9Ic_tAC-WJaXUks80b6JCBnrQ7D9tExe8eiqrBd-H",
    "audience":"https://fastapi.example.com",
    "grant_type":"client_credentials"
  }'

{
    "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJ0bUN4TERYb1M2TjA0WWxyZ2dBMyJ9.eyJpc3MiOiJodHRwczovL2Rldi1zd3AxN3l4ZGM3cDZ1bnFoLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJCM09ONTFvOHV1aWJ0dWFsTE5JcW9nY2RFcTlxQkN5RkBjbGllbnRzIiwiYXVkIjoiaHR0cHM6Ly9mYXN0YXBpLmV4YW1wbGUuY29tIiwiaWF0IjoxNzUwMzIyOTUzLCJleHAiOjE3NTA0MDkzNTMsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsImF6cCI6IkIzT041MW84dXVpYnR1YWxMTklxb2djZEVxOXFCQ3lGIiwicGVybWlzc2lvbnMiOltdfQ.V7X8KxEpy2IvvSi3i4NtD5wm__oE3fhAocNNf1Az1qgCiuEecczjkbPUeoRXV1ZfoLIni1fJuTIdJ29I8miRyBuz_u-BktpYtPuGh5g07IByYSS0olz4O55GS3XxMGgk-bYyfE71oKYP8cFOopwWtHmNEhHwMXWPIlbHRSSazfq4tYYZTI2Ufq8UKBor7AXm06TwFcVRSQRhCxJU83nBgnBXlLEIAfs1RhQmQobJLhgTrc4o6j2hm2Ax795sUGVLz8CDPO_Pr3Y07ck4oO7EHA7BkoRk880vLkxRyqLjGkVjlyhvVM5V2rezRywQC1OfdQ2snwW0ItMGq7jpCjaoPA",
    "expires_in": 86400,
    "token_type": "Bearer"
}

https://github.com/sunny7899/FastAPI-CRUD

pip install fastapi uvicorn python-dotenv requests jose[cryptography] sqlmodel 
pip3 install pipreqs

AUTH0_CLIENT_ID -> Application regular app
APIs domain is similar to base url Application
AUTH0_CLIENT_SECRET -> Application regular app
AUTH0_AUDIENCE -> APIs identifier Custom API
AUTH0_DOMAIN -> APIs base url

B3ON51o8uuibtualLNIqogcdEq9qBCyF - m2m clientid
DahLvx1QbK9oJLuiWgexIRu9Ic_tAC-WJaXUks80b6JCBnrQ7D9tExe8eiqrBd-H - secret

WP06JJjDmYruqp51NtlEriD7P7xwGw3z - normal user clientid
gBzXpLJc_8RrM3_OR1uR6SXQ7s3JmuOYIpGiPbE9d2NnTmgH1q1XG-3gF4Ja3aGX - secret
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
You just showed an auth user to read the object, what about auth0 m2m
show that an m2m app can access the system, since you have set up auth0 you must have seen a section where there is an m2m app which is also supposed to access the models but for now just reading the data 