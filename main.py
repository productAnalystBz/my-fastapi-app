from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Привет, Дима! 😊"}

@app.get("/hi/{name}")
def greet_name(name: str):
    return {"message": f"Привет, {name}! 🙂"}
