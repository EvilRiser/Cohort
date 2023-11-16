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


# You can call the above API like -
# http://localhost:8000/students?name=SSaha

##
# Request Bodies -
##


class MyBody(BaseModel):
    name: str
    age: int


"""
FastAPI knows that a request body param `req_body`
will be found, therefore will pass it as 
an argument in the function.

It knows this as `req_body` is of type `MyBody` (pydantic type)
"""


@app.post("/students") # POST API
async def fetch_name(req_body: MyBody):
    return {"studentName": req_body.name}

# You can call the above API with Postman and make a POST request with following JSON body -
# {
#   "name": "SSaha",
#   "age": 10
# }
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
