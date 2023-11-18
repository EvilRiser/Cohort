import datetime

from fastapi import FastAPI, status
from models import Student
import uvicorn
from database import students_data


tags_metadata = [
    {
        "name": "Students",
        "description": "Library Management System",
    },
    {
        "name": "Health Check",
        "description": "Health check",

    },
]

# app = FastAPI(openapi_url="/api/v1/openapi.json", docs_url="/documentation", openapi_tags=tags_metadata)

app = FastAPI()


@app.get("/students", tags=["Students"])
def get_student_details():
    """
    Fetches detail of all the student data
    :return:
    """
    return {}


@app.post("/students", tags=["Students"],response_model=Student, status_code=status.HTTP_201_CREATED,)
async def update_multiple_student_data(student: Student):
    """
    Update multiple student data
    :param student:
    :return:
    """
    try:
        # student = {
        #     "name": "ss",
        #     "date": datetime.datetime.now()
        # }
        result = await students_data.insert_one(student.model_dump(by_alias=True, exclude=["id"]))
        if result.acknowledged:
            return student
    except Exception as e:
        return {"error": True, "error_msg": e}


# @app.post("/students/{student_id}", tags=["Students"])
# def save_student_detail(student_id: int):
#     """
#     save student data into db
#     :param student_id:
#     :return:
#     """
#     return {"student_id": student_id}


@app.put("/students/{student_id}", tags=["Students"])
def update_student_data(student_id: int):
    """
    update student data in DB
    :param student_id:
    :return:
    """
    return {"student_id": student_id}


@app.delete("/students/{student_id}", tags=["Students"])
def delete_student_data(student_id: int):
    """
    delete student data from DB
    :param student_id:
    :return:
    """
    return {"student_id": student_id}


@app.get("/health", tags=["Health Check"])
def health_check():
    return 200


if __name__ == '__main__':
    uvicorn.run("Library_Management_System:app", host="localhost", port=8079, reload=True)
