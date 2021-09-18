from typing import Optional
from fastapi import FastAPI, HTTPException
from enum import Enum


class UserType(str, Enum):
    ADMIN = "admin"
    NORMAL = "normal"


app = FastAPI()
users = [
    {"name": "Trevor", "age": 30, "id": 1, 'user_type': UserType.ADMIN},
    {"name": "Foo", "age": 20, "id": 2, 'user_type': UserType.ADMIN},
    {"name": "Foo3", "age": 20, "id": 3, 'user_type': UserType.ADMIN},
    {"name": "Foo4", "age": 20, "id": 4, 'user_type': UserType.ADMIN},
    {"name": "Foo5", "age": 20, "id": 5, 'user_type': UserType.ADMIN},
    {"name": "Foo6", "age": 20, "id": 6, 'user_type': UserType.NORMAL},
    {"name": "Foo7", "age": 20, "id": 7, 'user_type': UserType.NORMAL},
    {"name": "Foo8", "age": 20, "id": 8, 'user_type': UserType.NORMAL},
    {"name": "Foo9", "age": 20, "id": 9, 'user_type': UserType.NORMAL},
    {"name": "Foo10", "age": 20, "id": 10, 'user_type': UserType.NORMAL},
]


@app.get('/users/{type}')
def users(type: UserType):
    if not type:
        return users
    return list(filter(lambda x: x['user_type'] == type, users))


@app.get('/users/{id}')
def user_detail(id: int):
    filterd = list(filter(lambda i: i["id"] == id, users))
    if filterd:
        return filterd[0]
    else:
        raise HTTPException(404)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', reload=True)
