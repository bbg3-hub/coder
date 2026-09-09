a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a <= b:
    if b <= c:
        print(f"Ascending order: {a}, {b}, {c}")
    else:
        if a <= c:
            print(f"Ascending order: {a}, {c}, {b}")
        else:
            print(f"Ascending order: {c}, {a}, {b}")
else:
    if a <= c:
        print(f"Ascending order: {b}, {a}, {c}")
    else:
        if b <= c:
            print(f"Ascending order: {b}, {c}, {a}")
        else:
            print(f"Ascending order: {c}, {b}, {a}")
