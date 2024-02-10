from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from api.contact_items import router as contact_router
from models import contact
from dependencies.database import engine

contact.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(contact_router, prefix='/contact')