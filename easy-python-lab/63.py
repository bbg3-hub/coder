# Problem 63: Find x^n (power) without using built-in pow function

def power(x, n):
    if n == 0:
        return 1
    elif n > 0:
        result = 1
        for _ in range(n):
            result *= x
        return result
    else:
        return 1 / power(x, -n)

x = float(input("Enter base (x): "))
n = int(input("Enter exponent (n): "))

result = power(x, n)
print(f"{x}^{n} = {result}")
