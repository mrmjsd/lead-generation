from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class EmployeeCreate(BaseModel):
    name: str
    code: str

class Employee(BaseModel):
    id: int
    name: str
    code: str

    class Config:
        from_attributes = True  # Allow from_orm usage