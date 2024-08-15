from fastapi import FastAPI

app = FastAPI()

@app.post("/")
async def hello_world():
    return {"message": "Hello World"}
