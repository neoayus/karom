import shutil 
import os 

from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from Conversion import convert_srt 

app = FastAPI()

@app.post("/upload")
async def upload(file: UploadFile = File(...)):

  upload_path = os.path.join("uploads", file.filename)

  # save file  
  with open(upload_path, "wb") as buffer: 
    shutil.copyfileobj(file.file, buffer)

  # convert file 
  new_file = convert_srt(upload_path)
  
  # return converted file 
  return FileResponse(
    path=new_file,
    filename=os.path.basename(new_file),
    media_type="text/plain"
  )
