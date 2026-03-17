from db import *

# ---------------- USERS ----------------
def list_users():
    return get_all_users()

def get_user(user_id: int):
    return get_user_by_id(user_id)

def search_users(name: str):
    return get_users_by_name(name)

def create_user(name, email):
    insert_user(name, email)

def update_user_business(user_id, name, email):
    update_user(user_id, name, email)

def delete_user_business(user_id):
    delete_user(user_id)

# ---------------- PROMPTS ----------------
def list_prompts():
    return get_all_prompts()

def get_prompt(prompt_id: int):
    return get_prompt_by_id(prompt_id)

def prompts_for_user(user_id: int):
    return get_prompts_by_user(user_id)

def create_prompt(text, version, user_id):
    insert_prompt(text, version, user_id)

def update_prompt_business(prompt_id, new_text):
    update_prompt(prompt_id, new_text)

def delete_prompt_business(prompt_id):
    delete_prompt(prompt_id)

# ---------------- AI MODELS ----------------
def list_models():
    return get_all_ai_models()

def get_model(model_id: int):
    return get_ai_model_by_id(model_id)

def search_models(provider: str):
    return get_models_by_provider(provider)

def create_model(name, provider):
    insert_ai_model(name, provider)

def update_model_business(model_id, name, provider):
    update_ai_model(model_id, name, provider)

def delete_model_business(model_id):
    delete_ai_model(model_id)

# ---------------- EXECUTIONS ----------------
def list_executions():
    return get_all_prompt_executions()

def get_execution(execution_id: int):
    return get_execution_by_id(execution_id)

def executions_for_prompt(prompt_id: int):
    return get_executions_by_prompt(prompt_id)

def create_execution(prompt_id, model_id, output):
    insert_prompt_execution(prompt_id, model_id, output)

def update_execution_business(execution_id, output):
    update_prompt_execution(execution_id, output)

def delete_execution_business(execution_id):
    delete_prompt_execution(execution_id)