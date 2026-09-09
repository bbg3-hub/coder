import math

def factorial(n):
    if n <= 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

x = float(input("Enter x (in radians): "))
terms = int(input("Enter number of terms: "))

sin_sum = 0

for i in range(terms):
    power = 2 * i + 1
    term = ((-1) ** i) * (x ** power) / factorial(power)
    sin_sum += term

print(f"sin({x}) using series: {sin_sum:.6f}")
print(f"sin({x}) using math.sin(): {math.sin(x):.6f}")
