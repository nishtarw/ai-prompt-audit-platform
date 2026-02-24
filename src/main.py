from db import (
    # Prompts
    get_all_prompts, insert_prompt, update_prompt, delete_prompt,
    # Users
    get_all_users, insert_user, update_user, delete_user,
    # AI Models
    get_all_ai_models, insert_ai_model, update_ai_model, delete_ai_model,
    # Prompt Executions
    get_all_prompt_executions, insert_prompt_execution, update_prompt_execution, delete_prompt_execution
)

def print_table(title, rows):
    print(f"\n--- {title} ---")
    for row in rows:
        print(row)

# --------------------------
# USERS CRUD
# --------------------------
print_table("Initial Users", get_all_users())

# CREATE temporary user
insert_user("Temp User", "tempuser@example.com")
users = get_all_users()
temp_user_id = users[-1][0]  # ID of the last inserted user

# UPDATE
update_user(temp_user_id, "Temp User Updated", "updated@example.com")
print_table("Users after INSERT & UPDATE", get_all_users())

# --------------------------
# AI MODELS CRUD
# --------------------------
print_table("Initial AI Models", get_all_ai_models())

# CREATE temporary AI model
insert_ai_model("Temp Model", "OpenAI")
ai_models = get_all_ai_models()
temp_model_id = ai_models[-1][0]

# UPDATE
update_ai_model(temp_model_id, "Temp Model Updated", "OpenAI v2")
print_table("AI Models after INSERT & UPDATE", get_all_ai_models())

# --------------------------
# PROMPTS CRUD
# --------------------------
print_table("Initial Prompts", get_all_prompts())

# CREATE using temp_user_id
insert_prompt("Temp Prompt", 1, temp_user_id)
prompts = get_all_prompts()
temp_prompt_id = prompts[-1][0]

# UPDATE
update_prompt(temp_prompt_id, "Temp Prompt Updated")
print_table("Prompts after INSERT & UPDATE", get_all_prompts())

# --------------------------
# PROMPT EXECUTIONS CRUD
# --------------------------
print_table("Initial Prompt Executions", get_all_prompt_executions())

# CREATE using temp_prompt_id and temp_model_id
insert_prompt_execution(temp_prompt_id, temp_model_id, "Temp execution result")
executions = get_all_prompt_executions()
temp_execution_id = executions[-1][0]

# UPDATE
update_prompt_execution(temp_execution_id, "Temp execution updated")
print_table("Prompt Executions after INSERT & UPDATE", get_all_prompt_executions())

# --------------------------
# DELETE in safe order
# --------------------------
delete_prompt_execution(temp_execution_id)
delete_prompt(temp_prompt_id)
delete_ai_model(temp_model_id)
delete_user(temp_user_id)

print_table("Users after DELETE", get_all_users())
print_table("AI Models after DELETE", get_all_ai_models())
print_table("Prompts after DELETE", get_all_prompts())
print_table("Prompt Executions after DELETE", get_all_prompt_executions())