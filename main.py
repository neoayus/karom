import os 
import shutil 

from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware 

from Conversion import convert_srt 

app = FastAPI()

# Allow frontend to access backend 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Directories 
UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.post("/upload")
async def upload(file: UploadFile = File(...)):

  upload_path = os.path.join("uploads", file.filename)

  # save file  
  with open(upload_path, "wb") as buffer: 
    shutil.copyfileobj(file.file, buffer)

  # convert file 
  new_file = convert_srt(upload_path)
  
  # return JSON with converted file info
  return{
    "original_file": file.filename, 
    "converted_file": os.path.basename(new_file),
    "converted_path": new_file 
  }

@app.get("/download/{filename}")
async def download_file(filename: str):
  # Build the full path of the converted file
  file_path = os.path.join(OUTPUT_DIR, filename)
  
  # Check if file already exists
  if not os.path.exists(file_path): 
    return {"error": "file not found"}
  
  # Return file content 
  return FileResponse(
    path=file_path,
    filename=os.path.basename(file_path),
    media_type="text/plain"
  )