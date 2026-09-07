a = 5
b = 10
print(f"Before: a={a}, b={b}")
a = a ^ b
b = a ^ b
a = a ^ b
print(f"After: a={a}, b={b}")
