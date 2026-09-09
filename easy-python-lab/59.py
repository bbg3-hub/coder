# Problem 59: Find LCM of two numbers

def gcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = lcm(a, b)
print(f"LCM of {a} and {b}: {result}")
