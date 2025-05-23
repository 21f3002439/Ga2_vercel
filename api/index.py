from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def index():
    return {
        "message": "wlcome to the FastAPI"
    }


@app.get("/api/params")
def details(request: Request):
    parameters = []

    for parameter_name in request.query_params.keys():
        parameter_values = request.query_params.getlist(parameter_name)
        for value in parameter_values:
            parameters.append(
                {
                    "key": parameter_name,
                    "val": value
                }
            )
        print(parameters)
    return {
        "parameters": parameters
    }



from pydantic import BaseModel 

class Service(BaseModel):
    name: str
    price: float 

services = []

@app.post("/api/create_service")
def create_service(service: Service):
    service_details = {
        "name": service.name,
        "price": service.price
    }
    services.append(service_details)
    return {
        "message": "Service created successfully",
        "service": service_details
    }

@app.get("/api/services")
def get_services():
    return {
        "services": services
    }

@app.delete("/api/delete_service/{service_id}")
def delete(service_id: int):
    if service_id < 0 or service_id >= len(services):
        return {
            "message": "Service not found"
        }
    delete_service = services.pop(service_id)
    return {
        "message": "Service deleted successfully",
        "service": delete_service
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
# To run the FastAPI server, use the following command in your terminal:
# uvicorn api.index:app --reload
# This will start the server at http://