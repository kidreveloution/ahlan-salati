import imp
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from mainDriver import mainFunc
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://192.168.50.189:8080",
    "http://127.0.0.1:8080",
    "https://ahlan-salati.surge.sh/",
    "https://ahlan-salati.surge.sh",
    "http://localhost:3000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def read_item():
    return ("Sucsuess")


@app.get("/latLong/")
async def read_item(lat: float,long:float,days:int):
    mainFunc(lat,long,days)
    return FileResponse ("/tmp/mySalat.ics",media_type="mySalat/ics",filename="mySalat.ics")
