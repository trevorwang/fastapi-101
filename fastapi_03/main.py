from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def hello():
    return {"message": "Hello World"}


@app.get('/users')
def get_users(limit: int, name: Optional[str] = None, skip: int = 0):
    users = [
        {"name": "Trevor", "age": 30, "id": 1},
        {"name": "Foo", "age": 20, "id": 2},
        {"name": "Foo3", "age": 20, "id": 3},
        {"name": "Foo4", "age": 20, "id": 4},
        {"name": "Foo5", "age": 20, "id": 5},
        {"name": "Foo6", "age": 20, "id": 6},
        {"name": "Foo7", "age": 20, "id": 7},
        {"name": "Foo8", "age": 20, "id": 8},
        {"name": "Foo9", "age": 20, "id": 9},
        {"name": "Foo10", "age": 20, "id": 10},
    ]
    return {
        "limit": limit,
        "skipt": skip,
        "name": name,
        "items": users[skip:skip+limit]
    }


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', reload=True)
