a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

if a == b == c:
    print(f"Triangle with sides {a}, {b}, {c} is Equilateral")
elif a == b or b == c or a == c:
    print(f"Triangle with sides {a}, {b}, {c} is Isosceles")
else:
    print(f"Triangle with sides {a}, {b}, {c} is Scalene")
