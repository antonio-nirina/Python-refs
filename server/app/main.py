from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.interfaces.controller.data_controller import data

app = FastAPI()
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(data,tags=['data'])



