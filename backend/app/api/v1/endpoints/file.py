from fastapi import APIRouter, Depends, HTTPException,File, UploadFile
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db  # Adjust based on your DB session retrieval method
import os
import shutil
from app.utils.constant import get_file_uploader_dir

router = APIRouter()
FILE_UPLOAD_DIR=get_file_uploader_dir()
@router.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    # Check if the file_name is provided and matches the uploaded file's name
    if not file.filename:
        raise HTTPException(status_code=400, detail="File name is required and must match the uploaded file.")

    # Define the location where the file will be saved
    file_location = os.path.join(FILE_UPLOAD_DIR, file.filename)
    
    # Save the file
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    return {"info": f"File '{file.filename}' saved at '{file_location}'"}

