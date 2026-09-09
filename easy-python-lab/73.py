numbers = []

while True:
    n = int(input("Enter a number (enter -1 to stop): "))
    
    if n == -1:
        break
    
    numbers.append(n)

if numbers:
    count = len(numbers)
    average = sum(numbers) / count
    
    print(f"Count of numbers: {count}")
    print(f"Average: {average:.2f}")
    print(f"Sum: {sum(numbers)}")
else:
    print("No numbers entered")
