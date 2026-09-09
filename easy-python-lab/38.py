# Problem 38: Check if 3-digit number is Armstrong number (e.g., 153)

n = int(input("Enter a 3-digit number: "))

if n < 100 or n > 999:
    print("Please enter a valid 3-digit number")
else:
    digits = [int(d) for d in str(n)]
    sum_of_cubes = sum(d**3 for d in digits)
    
    if sum_of_cubes == n:
        print(f"{n} is an Armstrong number")
    else:
        print(f"{n} is not an Armstrong number")
