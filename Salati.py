from fastapi import FastAPI, File, UploadFile
import shutil

docHeaderAPI = FastAPI()


@docHeaderAPI.get("/")
async def root():
    return {"message": "Hello World"}



@docHeaderAPI.post("/getsalat/lat:{lat}&long:{long}")
async def getsalat(lat,long):
