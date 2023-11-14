from typing import Union
from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/item_detail")
async def fetch_name(name: str):
    return {"itemName": name}

if __name__ == '__main__':
    uvicorn.run("app:app", host="localhost", port=8000, reload=True)

# The command uvicorn main:app refers to:
#
# main: the file main.py (the Python "module").
# app: the object created inside of main.py with the line app = FastAPI().
# --reload: make the server restart after code changes. Only do this for development.

# Another way to run
# config = uvicorn.Config("main:app", port=5000, log_level="info")
# server = uvicorn.Server(config)
# server.run()
