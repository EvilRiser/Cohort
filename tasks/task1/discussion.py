from fastapi import FastAPI


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
