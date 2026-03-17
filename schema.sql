CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL
);

CREATE TABLE ai_models (
    model_id SERIAL PRIMARY KEY,
    model_name VARCHAR(120) NOT NULL,
    provider VARCHAR(120) NOT NULL
);

CREATE TABLE prompts (
    prompt_id SERIAL PRIMARY KEY,
    prompt_text TEXT NOT NULL,
    version INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    CONSTRAINT fk_prompts_user
        FOREIGN KEY (user_id)
        REFERENCES users(user_id)
        ON DELETE CASCADE
);

CREATE TABLE prompt_executions (
    execution_id SERIAL PRIMARY KEY,
    prompt_id INTEGER NOT NULL,
    model_id INTEGER NOT NULL,
    output_text TEXT NOT NULL,
    executed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_exec_prompt
        FOREIGN KEY (prompt_id)
        REFERENCES prompts(prompt_id)
        ON DELETE CASCADE,
    CONSTRAINT fk_exec_model
        FOREIGN KEY (model_id)
        REFERENCES ai_models(model_id)
        ON DELETE CASCADE
);