"""Main module."""

# Python
from uuid import UUID
from datetime import date, datetime
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
    tweet_id: UUID = Field(...)
    content: str = Field(
        ...,
        min_length=1,
        max_length=256
    )
    created_at: datetime = Field(default=datetime.now())
    update_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)


@app.get(path='/')
def home():
    """Home page."""
    return {'Twitter API': 'Working!'}
