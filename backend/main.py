from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

import requests

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

PRIVATE_KEY = "dade907f-8575-4482-84f4-786e1e9eaade"


class User(BaseModel):
    username: str


@app.post('/authenticate')
async def authenticate(user: User):
    response = requests.put('https://api.chatengine.io/users/',
                            data={
                                "username": user.username,
                                "secret": user.username,
                                "first_name": user.username,
                            },
                            headers={"Private-Key": PRIVATE_KEY}
                            )
    return response.json()