# Todo API

A simple REST API built with FastAPI and Python.

## Features
- Create, read, update and delete todos
- Input validation with Pydantic
- Error handling with proper HTTP status codes

## Routes
| Method | Route | Description |
|--------|-------|-------------|
| GET | /todos | Get all todos |
| GET | /todos/{id} | Get single todo |
| POST | /todos | Create a todo |
| PUT | /todos/{id} | Mark todo as done |
| DELETE | /todos/{id} | Delete a todo |

## How to run
```bash
pip install fastapi uvicorn
python -m uvicorn todo:app --reload
```

Then open http://localhost:8000/docs