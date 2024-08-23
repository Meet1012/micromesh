from fastapi import FastAPI
app = FastAPI()

static_notes = [{"id":"1","Note":"Server 1"}]

@app.get("/notes")
def list_notes():
    return static_notes[0]