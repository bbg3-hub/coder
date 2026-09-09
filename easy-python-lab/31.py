month = int(input("Enter month number (1-12): "))

if month in [1, 3, 5, 7, 8, 10, 12]:
    print(f"Month {month} has 31 days")
elif month in [4, 6, 9, 11]:
    print(f"Month {month} has 30 days")
elif month == 2:
    print(f"Month {month} has 28/29 days (leap year dependent)")
else:
    print("Invalid month number")
