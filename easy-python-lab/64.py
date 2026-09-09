def factorial(n):
    if n <= 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

n = int(input("Enter N: "))

sum_factorials = 0

for i in range(1, n + 1):
    sum_factorials += factorial(i)

print(f"Sum of 1! + 2! + 3! + ... + {n}! = {sum_factorials}")
