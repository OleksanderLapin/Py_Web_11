from pydantic import BaseModel, EmailStr, Field
from datetime import date, datetime


class Contact(BaseModel):
    id: int = 1
    name: str
    surname: str
    email: EmailStr
    phone: str
    birthday: date
    
    class Config:
        orm_mode = True
        from_attributes=True
    
class ContactCreate(BaseModel):
    name: str = Field('John', min_length=2, max_length=22)
    surname: str = Field('Doe', min_length=2, max_length=22)
    email: EmailStr
    phone: str = Field('+380990001122')
    birthday: date

class ContactUpdate(BaseModel):
    name: str | None
    surname: str | None
    email: EmailStr | None
    phone: str | None
    birthday: date | None