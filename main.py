from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


@app.get("/")
def home():
    return {"message": "hello Bala"}


@app.get("/about")
def about():
    return {"name": "Bala", "goal": "backend engineer"}


@app.get("/skills")
def skills():
    return {"skills": ["Python", "FastAPI", "ECE"]}


@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"hello {name}"}


@app.get("/add")
def add(a: int, b: int):
    return {f"result : {a + b}"}


@app.get("/multiply")
def multiply(a: int, b: int):
    return {"result": a * b}


class Item(BaseModel):
    name: str
    price: float


@app.post("/items")
def create_item(item: Item):
    return {"received": item.name, "price": item.price}
