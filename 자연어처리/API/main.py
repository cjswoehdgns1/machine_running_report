#python -m uvicorn main:app --reload

from train import train_sentences
from return_sentence import return_similar_answer
from fastapi import FastAPI
from enum import Enum

from fastapi.templating import Jinja2Templates
from fastapi import Request
from time import time


class ModelName(str, Enum):
    sentence_transformer = "sentence_transformer"
    # resnet = "resnet"
    # lenet = "lenet"

app = FastAPI()

print("모델 준비 중")
s = time()
model, train_data  = train_sentences(5000)
print("모델 준비 완료까지 {:.2f}초 소요됨".format(time() - s))

templates = Jinja2Templates(directory="./")

@app.get("/")
async def root(request: Request):
	return templates.TemplateResponse("index.html",{"request":request})

@app.get("/items/{item_id}")
async def read_item(item_id: int, item_name: str):
    return {"item_id": item_id, "item_name": item_name}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName, req_param: str):

    if model_name is ModelName.sentence_transformer:
        return {"model_name": model_name, "req_param": req_param, "rep_param": return_similar_answer(model, train_data, req_param)}

    # if model_name.value == "lenet":
    #     return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}    