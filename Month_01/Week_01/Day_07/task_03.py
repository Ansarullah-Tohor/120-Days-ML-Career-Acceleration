x = 47
try:
    nums = int(input("Enter a number: "))
    print(x / nums)
except ZeroDivisionError:
    print("cant divide a number by zero")
finally:
    print("Execution Complete")