def gcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = gcd(a, b)
print(f"GCD/HCF of {a} and {b}: {result}")
