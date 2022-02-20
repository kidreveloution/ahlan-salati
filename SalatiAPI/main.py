import imp
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from mainDriver import mainFunc
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "file:///C:/Users/aladdin/Desktop/ahlan-salati/FrontEnd/Testing.html"
    " http://192.168.50.189:8080",
    "http://127.0.0.1:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_item():
    return ("Sucsuess")


@app.get("/latLong/")
async def read_item(lat: float,long:float):
    mainFunc(lat,long)
    return FileResponse ("/tmp/mySalat.ics",media_type="mySalat/ics",filename="mySalat.ics")
