user = {"id": 1}

print(f"email: {user.get("email")}")

safe_email = user.get("email", "gmail@gmail.com")
print(f"email accessed safely : {safe_email}")

print(f"id: {user.get("id")}")