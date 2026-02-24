from fastapi import FastAPI
from business import *

app = FastAPI()

# ---------------- USERS ----------------

@app.get("/users")
def get_users():
    return list_users()

@app.post("/users")
def add_user(name: str, email: str):
    create_user(name, email)
    return {"message": "User created"}

@app.put("/users/{user_id}")
def update_user_service(user_id: int, name: str, email: str):
    update_user_business(user_id, name, email)
    return {"message": "User updated"}

@app.delete("/users/{user_id}")
def delete_user_service(user_id: int):
    delete_user_business(user_id)
    return {"message": "User deleted"}


# ---------------- PROMPTS ----------------

@app.get("/prompts")
def get_prompts():
    return list_prompts()

@app.post("/prompts")
def add_prompt(text: str, version: int, user_id: int):
    create_prompt(text, version, user_id)
    return {"message": "Prompt created"}

@app.put("/prompts/{prompt_id}")
def update_prompt_service(prompt_id: int, text: str):
    update_prompt_business(prompt_id, text)
    return {"message": "Prompt updated"}

@app.delete("/prompts/{prompt_id}")
def delete_prompt_service(prompt_id: int):
    delete_prompt_business(prompt_id)
    return {"message": "Prompt deleted"}


# ---------------- AI MODELS ----------------

@app.get("/models")
def get_models():
    return list_models()

@app.post("/models")
def add_model(name: str, provider: str):
    create_model(name, provider)
    return {"message": "Model created"}

@app.put("/models/{model_id}")
def update_model_service(model_id: int, name: str, provider: str):
    update_model_business(model_id, name, provider)
    return {"message": "Model updated"}

@app.delete("/models/{model_id}")
def delete_model_service(model_id: int):
    delete_model_business(model_id)
    return {"message": "Model deleted"}


# ---------------- EXECUTIONS ----------------

@app.get("/executions")
def get_executions():
    return list_executions()

@app.post("/executions")
def add_execution(prompt_id: int, model_id: int, output: str):
    create_execution(prompt_id, model_id, output)
    return {"message": "Execution created"}

@app.put("/executions/{execution_id}")
def update_execution_service(execution_id: int, output: str):
    update_execution_business(execution_id, output)
    return {"message": "Execution updated"}

@app.delete("/executions/{execution_id}")
def delete_execution_service(execution_id: int):
    delete_execution_business(execution_id)
    return {"message": "Execution deleted"}


# ---------------- HOSTING NOTES ----------------
"""
To run locally:

1. Open terminal
2. Navigate to src folder
3. Run:

uvicorn service:app --reload

This starts the API at:
http://127.0.0.1:8000

Swagger testing UI:
http://127.0.0.1:8000/docs

To host:
- Can use Render, Railway, or AWS
- Example:
    pip install fastapi uvicorn
    deploy using Docker or Python web service
"""