from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

##
# Basic API Router -
##


@app.get("/")
async def hello():
    # FastAPI auto converts python dict/list objects to JSON responses...
    return {"hello": "world"}

##
# URL Params -
##
"""
FastAPI knows that a variable `student_id`
will be found, therefore will pass it as 
an argument in the function.
"""


@app.get("/{student_id}")
async def fetch_id(student_id):
    return {"studentId": student_id}

##
# Query Params -
##
"""
FastAPI knows that a query param `name`
will be found, therefore will pass it as 
an argument in the function.

It knows this as `name` is of type `str` (inbuilt type)
"""


@app.get("/students")
async def fetch_name(name: str):
    return {"studentName": name}

##
# Body
##
"""
For FastAPI to show the body we use pydantic class to specify body schema and
pass that class as argument in function 
"""


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):  # here item is the body of put method
    return {"item_name": item.name, "item_id": item_id}

# You can call the above API like -
# http://localhost:8000/students?name=SSaha
