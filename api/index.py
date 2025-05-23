# from fastapi import FastAPI, Request
# from fastapi.middleware.cors import CORSMiddleware


# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# @app.get("/")
# def index():
#     return {
#         "message": "Student Marks API. Use /api?name=X&name=Y to get marks."
#     }


# # Get the directory of the current file
# current_dir = os.path.dirname(os.path.abspath(__file__))
# # Load student marks data from the same directory as this file
# with open(os.path.join(current_dir, 'q-vercel-python.json')) as f:
#     students_data = json.load(f)





# @app.get("/api/params")
# def details(request: Request):
#     parameters = []

#     for parameter_name in request.query_params.keys():
#         parameter_values = request.query_params.getlist(parameter_name)
#         for value in parameter_values:
#             parameters.append(
#                 {
#                     "key": parameter_name,
#                     "val": value
#                 }
#             )
#         print(parameters)
#     return {
#         "parameters": parameters
#     }



# from pydantic import BaseModel 

# class Service(BaseModel):
#     name: str
#     price: float 

# services = []

# @app.post("/api/create_service")
# def create_service(service: Service):
#     service_details = {
#         "name": service.name,
#         "price": service.price
#     }
#     services.append(service_details)
#     return {
#         "message": "Service created successfully",
#         "service": service_details
#     }

# @app.get("/api/services")
# def get_services():
#     return {
#         "services": services
#     }

# @app.delete("/api/delete_service/{service_id}")
# def delete(service_id: int):
#     if service_id < 0 or service_id >= len(services):
#         return {
#             "message": "Service not found"
#         }
#     delete_service = services.pop(service_id)
#     return {
#         "message": "Service deleted successfully",
#         "service": delete_service
#     }

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)
# To run the FastAPI server, use the following command in your terminal:
# uvicorn api.index:app --reload
# This will start the server at http://





from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import json
import os

# Initialize FastAPI app
app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["GET"],  # Only allow GET requests
    allow_headers=["*"],
)

# Get the directory of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
# Load student marks data from the same directory as this file
with open(os.path.join(current_dir, 'q-vercel-python.json')) as f:
    students_data = json.load(f)

@app.get("/api")
async def get_marks(name: List[str] = Query(None)):
    """
    Get marks for one or more students by name.
    Example: /api?name=John&name=Alice
    """
    if not name:
        return {"error": "Please provide at least one name"}
    
    marks = []
    for student_name in name:
        # Look for the student in the data
        mark = next((student["marks"] for student in students_data 
                     if student["name"].lower() == student_name.lower()), None)
        marks.append(mark)
    
    return {"marks": marks}

@app.get("/")
async def root():
    return {"message": "Student Marks API. Use /api?name=X&name=Y to get marks."}

# This allows running the app with Uvicorn directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("index:app", host="0.0.0.0", port=8000, reload=True)