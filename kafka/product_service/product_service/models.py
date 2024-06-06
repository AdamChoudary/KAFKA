from fastapi import Form
from pydantic import BaseModel
from sqlmodel import SQLModel, Field
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated


class Product (SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(index=True , unique=True , max_length=30 , min_length=3)
    price: float
    quantity: int

class Product_Create (BaseModel):
    name: str
    price: float
    quantity: int

class Product_Update(BaseModel):
    name: str
    price: float
    quantity: int