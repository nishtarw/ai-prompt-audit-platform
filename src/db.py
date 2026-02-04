import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="ai_prompt_audit",
        user="postgres",
        password="Nishtarw2005!"  # keep quotes
    )

# READ
def get_all_prompts():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM prompts ORDER BY prompt_id;")
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results

# CREATE
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

# UPDATE
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

# DELETE
def delete_prompt(prompt_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM prompts WHERE prompt_id = %s",
        (prompt_id,)
    )
    conn.commit()
    cur.close()
    conn.close()
