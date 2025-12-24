try:
    nums = int(input("Enter a number: "))
    if nums < 0:
        raise ValueError("No negatives")

    print(nums)
except ValueError as error:
    print(f"Error: {error}")