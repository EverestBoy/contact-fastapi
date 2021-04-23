from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

# adding cors
middleware = [
    Middleware(CORSMiddleware, 
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
]

app = FastAPI(middleware=middleware)



class Parameters(BaseModel):
    name: str
    email: EmailStr
    number: float
    message: str
    subject: str



@app.post("/contact_form")
async def read_item(param: Parameters):
    response = {}
    response['success'] = True
    response['data'] = param
    print(param)
    return response
