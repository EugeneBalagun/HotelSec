# app/schemas.py
from pydantic import BaseModel, EmailStr

class LeadCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str

class LeadResponseMessage(BaseModel):
    message: str
    lead_id: int
