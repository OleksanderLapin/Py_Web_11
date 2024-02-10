from sqlalchemy import Column, Integer, String, DateTime
from dependencies.database import Base


class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, index=True)