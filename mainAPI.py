import imp
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from main import mainFunc
from fastapi.responses import FileResponse


app = FastAPI()


@app.post("/latLong/")
async def read_item(lat: int,long:int):
    mainFunc(lat,long)
    return FileResponse("myics.ics")
