from typing import Union
from fastapi import FastAPI, Response, Request

app = FastAPI()

# Import local module
from .helper import api_builder

@app.get("/", status_code=200)
def status(response: Response):
    return api_builder.builder("Hello World! hzlnqodrey Sentiment API Work", response.status_code)