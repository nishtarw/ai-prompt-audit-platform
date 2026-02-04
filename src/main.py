from db import (
    get_all_prompts,
    insert_prompt,
    update_prompt,
    delete_prompt
)

def print_prompts(title):
    print(f"\n{title}")
    for p in get_all_prompts():
        print(p)

# READ (initial)
print_prompts("Initial prompts:")

# CREATE
print("\nCreating a new prompt...")
insert_prompt("CRUD demo prompt", 1, 1)
print_prompts("After CREATE:")

# UPDATE
print("\nUpdating prompt with ID 1...")
update_prompt(1, "UPDATED prompt text (CRUD demo)")
print_prompts("After UPDATE:")

# DELETE
# Use the highest ID you see in the output above if needed
print("\nDeleting prompt with ID 7...")
delete_prompt(7)
print_prompts("After DELETE:")
