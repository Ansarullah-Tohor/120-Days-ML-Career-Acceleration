try:
    age = int(input("Enter age: "))
    print(f" age is {age} years")
except ValueError:
    print("Numbers only")