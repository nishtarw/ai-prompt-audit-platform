import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="ai_prompt_audit",
        user="postgres",
        password="Nishtarw2005!"
    )

def get_all_prompts():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM prompts;")
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
