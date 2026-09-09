# Problem 48: Count the number of digits in a number

n = int(input("Enter a number: "))

count = 0
temp = abs(n)  # Handle negative numbers

if temp == 0:
    count = 1
else:
    while temp > 0:
        count += 1
        temp //= 10

print(f"Number of digits in {n}: {count}")
