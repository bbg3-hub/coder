n = input("Enter a number: ")

digits = [int(d) for d in n if d.isdigit()]

if digits:
    largest = max(digits)
    smallest = min(digits)
    
    print(f"Largest digit: {largest}")
    print(f"Smallest digit: {smallest}")
else:
    print("No digits found")
