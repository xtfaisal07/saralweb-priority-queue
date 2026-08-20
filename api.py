from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pathlib import Path
from database.db import Database
from fastapi import HTTPException

from module import PriorityQueue

app = FastAPI(title="Persistent Priority Queue API")

@app.get("/")
def home():
    return {
        "project": "Persistent Priority Queue API",
        "status": "running",
        "docs": "/docs"
    }

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
    "http://localhost:5173",
    "https://saralweb-pq-web.vercel.app",  # replace with your real Vercel URL later
],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
def initialize_database():
    db = Database()

    schema_path = Path(__file__).parent / "database" / "schema.sql"

    with open(schema_path, "r") as f:
        db.execute(f.read())

    db.close()


initialize_database()
pq = PriorityQueue()


class Task(BaseModel):
    value: str
    priority: int


class UpdateTask(BaseModel):
    priority: int


@app.get("/tasks")
def get_tasks():
    return pq.display()


@app.post("/insert")
def insert(task: Task):
    node = pq.insert(task.value, task.priority)
    return {
        "id": node.id,
        "value": node.value,
        "priority": node.priority
    }


@app.get("/peek")
def peek():
    data = pq.peek()

    return {
        "min": {
            "id": data["min"].id,
            "value": data["min"].value,
            "priority": data["min"].priority,
        },
        "max": {
            "id": data["max"].id,
            "value": data["max"].value,
            "priority": data["max"].priority,
        }
    }



@app.post("/extract-min")
def extract_min():
    try:
        node = pq.extract_min()
        return {
            "id": node.id,
            "value": node.value,
            "priority": node.priority
        }
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@app.post("/extract-max")
def extract_max():
    try:
        node = pq.extract_max()
        return {
            "id": node.id,
            "value": node.value,
            "priority": node.priority
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.put("/update/{node_id}")
def update(node_id: int, task: UpdateTask):
    try:
        pq.update(node_id, task.priority)
        return {"message": "updated"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/delete/{node_id}")
def delete(node_id: int):
    try:
        pq.delete(node_id)
        return {"message": "deleted"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))