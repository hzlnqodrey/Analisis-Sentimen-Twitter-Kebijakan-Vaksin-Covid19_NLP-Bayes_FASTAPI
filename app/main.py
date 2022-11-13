from typing import Union

from fastapi import FastAPI, Response, Request

app = FastAPI()

@app.get("/", status_code=200)
async def status(response: Response):
    return {"Hello" : "World"}