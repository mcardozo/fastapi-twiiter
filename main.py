"""Main module."""

# Python
from uuid import UUID
from datetime import date
from typing import Optional

# FastAPI
from fastapi import FastAPI

# Pydantic
from pydantic import BaseModel, EmailStr, Field

app = FastAPI()


# Models
class UserBase(BaseModel):
    """User Model."""
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)


class UserLogin(UserBase):
    """User Login model."""
    password: str = Field(
        ...,
        min_length=8
    )


class User(UserBase):
    """User model."""
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    birth_date: Optional[date] = Field(default=None)


class Tweet(BaseModel):
    """Tweet model."""
    pass


@app.get(path='/')
def home():
    """Home page."""
    return {'Twitter API': 'Working!'}
