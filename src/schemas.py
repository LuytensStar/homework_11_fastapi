from datetime import date
from pydantic import BaseModel,Field
from typing import List, Optional

class ContactModel(BaseModel):
    id: int
    name: str = Field(max_length=50, description="Name")
    surname: str = Field(max_length=50, description="Surname")
    electronic_mail: str = Field(max_length=100, description="Email")
    phone_number: str = Field(max_length=20, description="Phone number")
    birth_date: date = Field(description="Date of birth")
    additional_info: Optional[str] = Field( description="Additional info")

class ContactResponse(BaseModel):
    id: int
    name: str
    surname: str
    electronic_mail: str
    phone_number: str
    birth_date: date
    additional_info: Optional[str]