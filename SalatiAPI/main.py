import imp
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from mainDriver import mainFunc
from fastapi.responses import FileResponse


app = FastAPI()


@app.get("/")
async def read_item():
    return ("Sucsuess")


@app.get("/latLong/")
async def read_item(lat: int,long:int):
    mainFunc(lat,long)
    return FileResponse("/tmp/mySalat.ics")
