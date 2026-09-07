a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

# Triangle inequality: sum of any two sides > third side
if a + b > c and b + c > a and a + c > b:
    print(f"Sides {a}, {b}, {c} can form a valid triangle")
else:
    print(f"Sides {a}, {b}, {c} cannot form a valid triangle")
