from typing import Union
from fastapi import FastAPI, Response, Request

app = FastAPI()

# Import local module
from .helper import api_builder

# Index
@app.get("/", status_code=200)
def status(response: Response):
    return api_builder.builder("Hello World! hzlnqodrey Sentiment API Work", response.status_code)

# Predict

# Example Path params & Query
@app.get("/items/{item_id}", status_code=200)
def read_item(response: Response, item_id: int, q: Union[str, None] = None):
    result = []

    result.append({
        "item_id": item_id,
        "q": q
    })

    return api_builder.builder(result, response.status_code)
