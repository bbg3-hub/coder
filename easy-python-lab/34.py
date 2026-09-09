import math

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

if a == 0:
    print("Not a quadratic equation")
else:
    discriminant = b * b - 4 * a * c
    
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"Real and distinct roots: {root1}, {root2}")
    elif discriminant == 0:
        root = -b / (2 * a)
        print(f"Real and equal roots: {root}")
    else:
        real_part = -b / (2 * a)
        imag_part = math.sqrt(-discriminant) / (2 * a)
        print(f"Imaginary roots: {real_part}+{imag_part}i and {real_part}-{imag_part}i")
