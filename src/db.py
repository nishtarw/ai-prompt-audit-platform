import psycopg2

# -----------------------
# DATABASE CONNECTION
# -----------------------
def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="ai_prompt_audit",
        user="postgres",
        password="Nishtarw2005!"
    )

# -----------------------
# PROMPTS TABLE
# -----------------------
def get_all_prompts():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM prompts ORDER BY prompt_id;")
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results

def insert_prompt(prompt_text, version, user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO prompts (prompt_text, version, user_id) VALUES (%s, %s, %s)",
        (prompt_text, version, user_id)
    )
    conn.commit()
    cur.close()
    conn.close()

def update_prompt(prompt_id, new_text):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE prompts SET prompt_text = %s WHERE prompt_id = %s",
        (new_text, prompt_id)
    )
    conn.commit()
    cur.close()
    conn.close()

def delete_prompt(prompt_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM prompts WHERE prompt_id = %s", (prompt_id,))
    conn.commit()
    cur.close()
    conn.close()

# -----------------------
# USERS TABLE
# -----------------------
def get_all_users():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users ORDER BY user_id;")
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results

def insert_user(name, email):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO users (name, email) VALUES (%s, %s)",
        (name, email)
    )
    conn.commit()
    cur.close()
    conn.close()

def update_user(user_id, new_name, new_email):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE users SET name = %s, email = %s WHERE user_id = %s",
        (new_name, new_email, user_id)
    )
    conn.commit()
    cur.close()
    conn.close()

def delete_user(user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
    conn.commit()
    cur.close()
    conn.close()

# -----------------------
# AI_MODELS TABLE
# -----------------------
def get_all_ai_models():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM ai_models ORDER BY model_id;")
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results

def insert_ai_model(model_name, provider):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO ai_models (model_name, provider) VALUES (%s, %s)",
        (model_name, provider)
    )
    conn.commit()
    cur.close()
    conn.close()

def update_ai_model(model_id, new_name, new_provider):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE ai_models SET model_name = %s, provider = %s WHERE model_id = %s",
        (new_name, new_provider, model_id)
    )
    conn.commit()
    cur.close()
    conn.close()

def delete_ai_model(model_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM ai_models WHERE model_id = %s", (model_id,))
    conn.commit()
    cur.close()
    conn.close()

# -----------------------
# PROMPT_EXECUTIONS TABLE
# -----------------------
def get_all_prompt_executions():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM prompt_executions ORDER BY execution_id;")
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results

def insert_prompt_execution(prompt_id, model_id, output_text):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO prompt_executions (prompt_id, model_id, output_text) VALUES (%s, %s, %s)",
        (prompt_id, model_id, output_text)
    )
    conn.commit()
    cur.close()
    conn.close()

def update_prompt_execution(execution_id, new_output_text):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE prompt_executions SET output_text = %s WHERE execution_id = %s",
        (new_output_text, execution_id)
    )
    conn.commit()
    cur.close()
    conn.close()

def delete_prompt_execution(execution_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM prompt_executions WHERE execution_id = %s", (execution_id,))
    conn.commit()
    cur.close()
    conn.close()