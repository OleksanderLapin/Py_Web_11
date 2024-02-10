from sqlalchemy import Column, String, Integer, Date
from .base import BaseModel, Base

class ContactDB(BaseModel):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    surname = Column(String, index=True)
    email = Column(String, index=True)
    phone = Column(String, index=True)
    birthday = Column(Date)
