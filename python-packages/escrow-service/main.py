from enum import Enum
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    match model_name:
        case ModelName.alexnet:
            return {"model_name": model_name, "message": "Deep Learning FTW!"}
        case ModelName.resnet:
            return {"model_name": model_name, "message": "LeCNN all the images"}
        case ModelName.lenet:
            return {"model_name": model_name, "message": "Have some residuals"}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
items_with_id = [{"id": index, **item} for index, item in enumerate(fake_items_db)]


@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    return items_with_id[skip : skip + limit]


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return next(x for x in items_with_id if x.get("id") == item_id)
