"""Main module."""

# FastAPI
from fastapi import FastAPI


app = FastAPI()

@app.get(path='/')
def home():
    """Home page."""
    return {'Twitter API': 'Working!'}
