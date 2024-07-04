from fastapi import FastAPI
from celery.result import AsyncResult
from tasks import add
from celery_config import celery_app

app = FastAPI()

@app.post("/tasks")
def run_task(x: int, y: int):
    task = add.apply_async(args=(x, y))
    return {"task_id": task.id}

@app.get("/tasks/{task_id}")
def get_task_status(task_id: str):
    task_result = AsyncResult(task_id, app=celery_app)
    if task_result.state == 'PENDING':
        return {"status": task_result.state}
    elif task_result.state != 'FAILURE':
        return {"status": task_result.state, "result": task_result.result}
    else:
        return {"status": task_result.state, "error": str(task_result.info)}
