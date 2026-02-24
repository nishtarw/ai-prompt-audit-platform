from db import *

# USERS
def list_users():
    return get_all_users()

def create_user(name, email):
    insert_user(name, email)

def update_user_business(user_id, name, email):
    update_user(user_id, name, email)

def delete_user_business(user_id):
    delete_user(user_id)


# PROMPTS
def list_prompts():
    return get_all_prompts()

def create_prompt(text, version, user_id):
    insert_prompt(text, version, user_id)

def update_prompt_business(prompt_id, new_text):
    update_prompt(prompt_id, new_text)

def delete_prompt_business(prompt_id):
    delete_prompt(prompt_id)


# AI MODELS
def list_models():
    return get_all_ai_models()

def create_model(name, provider):
    insert_ai_model(name, provider)

def update_model_business(model_id, name, provider):
    update_ai_model(model_id, name, provider)

def delete_model_business(model_id):
    delete_ai_model(model_id)


# EXECUTIONS
def list_executions():
    return get_all_prompt_executions()

def create_execution(prompt_id, model_id, output):
    insert_prompt_execution(prompt_id, model_id, output)

def update_execution_business(execution_id, output):
    update_prompt_execution(execution_id, output)

def delete_execution_business(execution_id):
    delete_prompt_execution(execution_id)