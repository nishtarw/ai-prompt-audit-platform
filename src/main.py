from db import get_all_prompts, insert_prompt

print("HELLO — MAIN.PY IS RUNNING")

print("Existing prompts:")
prompts = get_all_prompts()
for p in prompts:
    print(p)

print("\nInserting a new prompt...")
insert_prompt("Explain what SQL injection is", 1, 1)

print("\nUpdated prompts:")
prompts = get_all_prompts()
for p in prompts:
    print(p)
