from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

todos = []
id_counter = 1


@app.get("/todos")
def get_todos():
    return {"todos": todos}


class Todo(BaseModel):
    title: str
    done: bool = False


@app.post("/todos")
def create_todo(todo: Todo):
    global id_counter
    new_todo = {"id": id_counter, "title": todo.title, "done": todo.done}
    todos.append(new_todo)
    id_counter += 1
    return {"meassage": "Todo added", "todo": todo}


@app.delete("/todos/{id}")
def delete_todo(id: int):
    for todo in todos:
        if todo["id"] == id:
            todos.remove(todo)
            return {"message": "Todo Deleted"}

    raise HTTPException(status_code=404, detail="todo not found")


@app.put("/todos/{id}")
def put_todo(id: int):
    for todo in todos:
        if todo["id"] == id:
            todo["done"] = True
            return todo

    raise HTTPException(status_code=404, detail="todo not found")


@app.get("/todos/{id}")
def get_single_todo(id: int):
    for todo in todos:
        if todo["id"] == id:
            return todo
        
    raise HTTPException(status_code=404, detail="todo not found")
