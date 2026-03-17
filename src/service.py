from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from business import *

app = FastAPI()

# Allow browser frontend to call API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- USERS ----------------

@app.get("/users")
def get_users():
    return list_users()

@app.get("/users/search")
def search_users_service(name: str):
    return search_users(name)

@app.get("/users/{user_id}")
def get_user_service(user_id: int):
    user = get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

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

@app.get("/prompts/by-user/{user_id}")
def prompts_by_user_service(user_id: int):
    return prompts_for_user(user_id)

@app.get("/prompts/{prompt_id}")
def get_prompt_service(prompt_id: int):
    prompt = get_prompt(prompt_id)
    if not prompt:
        raise HTTPException(status_code=404, detail="Prompt not found")
    return prompt

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

@app.get("/models/search")
def search_models_service(provider: str):
    return search_models(provider)

@app.get("/models/{model_id}")
def get_model_service(model_id: int):
    model = get_model(model_id)
    if not model:
        raise HTTPException(status_code=404, detail="Model not found")
    return model

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

@app.get("/executions/by-prompt/{prompt_id}")
def executions_by_prompt_service(prompt_id: int):
    return executions_for_prompt(prompt_id)

@app.get("/executions/{execution_id}")
def get_execution_service(execution_id: int):
    execution = get_execution(execution_id)
    if not execution:
        raise HTTPException(status_code=404, detail="Execution not found")
    return execution

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


"""
To run locally:
1) cd src
2) uvicorn service:app --reload
API: http://127.0.0.1:8000
Docs: http://127.0.0.1:8000/docs
"""