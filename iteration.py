'''
Goal: Iterate over dictionaries.
'''

# Create a 'users' dictionary with the following pairs:
users: dict[str, str] = {
    "Alice" : "admin",
    "Bob" : "user",
    "Charlie" : "guest"
}

# Iterate over the dictionary and print each pair in the format: "Username: Alice - Role: admin"
for username, role in users.items():
    print(f"Username: {username} - Role: {role}")

# Check if "Bob" is a present key
is_bob_presente = "Bob" in users
print(f"Bob is there: {is_bob_presente}")

# Print all keys (usernames)
print(f"Usernames: {users.keys()}")

# Print all values (roles)
print(f"Roles: {users.values()}")