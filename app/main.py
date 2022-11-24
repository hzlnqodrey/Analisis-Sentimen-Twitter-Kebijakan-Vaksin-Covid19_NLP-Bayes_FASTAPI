import uvicorn
from typing import Union
from fastapi import FastAPI, Response, Request
from pydantic import BaseModel
import pandas as pd
import os

# Import local module
from .helper import api_builder

app = FastAPI(debug=True)

# Index
@app.get("/", status_code=200)
def status(response: Response):
    return api_builder.builder("Hello World! hzlnqodrey Sentiment API Work", response.status_code)

# Predict
@app.get("/predict", status_code=200)
def predict(response: Response):
    # fetch data
    data = pd.read_csv('./app/data/new_hasil_klasifikasi_naive_bayes_data_tweet_8k.csv')
    # fetch text_asli
    data2 = pd.read_csv('./app/data/tweets_covid_dataset_50k_raw_noindex.csv', engine='python')
    data2.drop(['Tanggal', 'Username'], axis=1, inplace=True)
    data2[data2.isna().any(axis=1)]
    data2 = data2.drop(labels=16413, axis=0) # drop null data
    data2 = data2.drop(data2.index[8000:], axis=0) # trim to 8k data

    # insert text column data2 to data
    data.insert(0, column="Text_Asli", value=data2['Text'])

    result = []
    # text_clean = text_english = nlp = bayes = []
    
    for index, row in list(data.iterrows()):
        result.append(row)


    return api_builder.builder(result, response.status_code)

# --------------------------------------------------------------------------------------------------------------------
class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

# Example Path params & Query
@app.get("/items/{item_id}", status_code=200)
def read_item(response: Response, item_id: int, q: Union[str, None] = None):
    result = []

    result.append({
        "item_id": item_id,
        "q": q
    })

    return api_builder.builder(result, response.status_code)

@app.put("/items/{item_id}", status_code=200)
def update_item(response: Response, item_id: int, item: Item):
    result = []
    
    result.append({
        "item_id": item_id,
        "item_name": item.name
    })

    return api_builder.builder(result, response.status_code)

# --------------------------------------------------------------------------------------------------------------------

### Debugging
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port="9000")

