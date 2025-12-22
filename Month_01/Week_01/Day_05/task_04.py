default = {"theme": "light","audio": "on"}

user_pref = {"theme": "dark"}
# update method
default_copy = default.copy()
default_copy.update(user_pref)
print(f"before using update method: {default}")
print(f"merged using update method: {default_copy}")