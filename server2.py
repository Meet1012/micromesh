from fastapi import FastAPI

app = FastAPI()

tasks = [{"id":"1","task":"Server 2"}]

@app.get("/tasks")
def Get_Tasks():
    return tasks[0]