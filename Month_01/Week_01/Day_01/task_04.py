total_second=int(input("Enter the total number of seconds:"))

hour=total_second//3600
remainder_second=total_second%3600
minute=remainder_second//60
second=remainder_second%60

print(f"Hour={hour} Minute={minute} Second={second}")