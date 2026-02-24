import requests

BASE_URL = "http://127.0.0.1:8000"

def print_response(title, response):
    print(f"\n--- {title} ---")
    print(response.json())

# ---------------- USERS ----------------
print("\n### USERS CRUD ###")

# CREATE
user_data = {"name": "Temp User", "email": "tempuser@example.com"}
response = requests.post(f"{BASE_URL}/users", params=user_data)
print_response("Create User", response)

# GET
response = requests.get(f"{BASE_URL}/users")
print_response("List Users", response)
temp_user_id = response.json()[-1][0]

# UPDATE
update_data = {"name": "Temp User Updated", "email": "updated@example.com"}
response = requests.put(f"{BASE_URL}/users/{temp_user_id}", params=update_data)
print_response("Update User", response)

# GET after update
response = requests.get(f"{BASE_URL}/users")
print_response("List Users After Update", response)

# ---------------- AI MODELS ----------------
print("\n### AI MODELS CRUD ###")

# CREATE
model_data = {"name": "Temp Model", "provider": "OpenAI"}
response = requests.post(f"{BASE_URL}/models", params=model_data)
print_response("Create Model", response)

# GET
response = requests.get(f"{BASE_URL}/models")
print_response("List Models", response)
temp_model_id = response.json()[-1][0]

# UPDATE
update_model_data = {"name": "Temp Model Updated", "provider": "OpenAI v2"}
response = requests.put(f"{BASE_URL}/models/{temp_model_id}", params=update_model_data)
print_response("Update Model", response)

# GET after update
response = requests.get(f"{BASE_URL}/models")
print_response("List Models After Update", response)

# ---------------- PROMPTS ----------------
print("\n### PROMPTS CRUD ###")

# CREATE
prompt_data = {"text": "Temp Prompt", "version": 1, "user_id": temp_user_id}
response = requests.post(f"{BASE_URL}/prompts", params=prompt_data)
print_response("Create Prompt", response)

# GET
response = requests.get(f"{BASE_URL}/prompts")
print_response("List Prompts", response)
temp_prompt_id = response.json()[-1][0]

# UPDATE
update_prompt_data = {"text": "Temp Prompt Updated"}
response = requests.put(f"{BASE_URL}/prompts/{temp_prompt_id}", params=update_prompt_data)
print_response("Update Prompt", response)

# GET after update
response = requests.get(f"{BASE_URL}/prompts")
print_response("List Prompts After Update", response)

# ---------------- EXECUTIONS ----------------
print("\n### EXECUTIONS CRUD ###")

# CREATE
execution_data = {"prompt_id": temp_prompt_id, "model_id": temp_model_id, "output": "Temp execution result"}
response = requests.post(f"{BASE_URL}/executions", params=execution_data)
print_response("Create Execution", response)

# GET
response = requests.get(f"{BASE_URL}/executions")
print_response("List Executions", response)
temp_execution_id = response.json()[-1][0]

# UPDATE
update_execution_data = {"output": "Temp execution updated"}
response = requests.put(f"{BASE_URL}/executions/{temp_execution_id}", params=update_execution_data)
print_response("Update Execution", response)

# GET after update
response = requests.get(f"{BASE_URL}/executions")
print_response("List Executions After Update", response)

# ---------------- DELETE ----------------
print("\n### DELETE ALL TEMP RECORDS ###")

response = requests.delete(f"{BASE_URL}/executions/{temp_execution_id}")
print_response("Delete Execution", response)

response = requests.delete(f"{BASE_URL}/prompts/{temp_prompt_id}")
print_response("Delete Prompt", response)

response = requests.delete(f"{BASE_URL}/models/{temp_model_id}")
print_response("Delete Model", response)

response = requests.delete(f"{BASE_URL}/users/{temp_user_id}")
print_response("Delete User", response)

# Final GET to confirm deletion
print_response("Users After Delete", requests.get(f"{BASE_URL}/users"))
print_response("Models After Delete", requests.get(f"{BASE_URL}/models"))
print_response("Prompts After Delete", requests.get(f"{BASE_URL}/prompts"))
print_response("Executions After Delete", requests.get(f"{BASE_URL}/executions"))