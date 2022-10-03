from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

# 1. Define an API object
app = FastAPI()


# 2. Define data type
class Msg(BaseModel):
    msg: str


# 3. Map HTTP method and path to python function
@app.get("/")
async def root():
    return {"message": "Hello World. Welcome to the API home page!"}


@app.get("/path")
async def function_demo_get():
    return {"message": "This is /path endpoint, use post request to transform text to uppercase"}


@app.post("/path")
async def function_demo_post(inp: Msg):
    return {"message": inp.msg.upper()}


@app.get("/path/{path_id}")
async def function_demo_get_path_id(path_id: str):
    return {"message": f"This is /path/{path_id} endpoint, use post request to retrieve result"}

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}


# 4. Start the API application (on command line)
