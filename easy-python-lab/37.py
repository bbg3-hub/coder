x = float(input("Enter x-coordinate: "))
y = float(input("Enter y-coordinate: "))

if x > 0 and y > 0:
    print(f"Point ({x}, {y}) is in Quadrant I")
elif x < 0 and y > 0:
    print(f"Point ({x}, {y}) is in Quadrant II")
elif x < 0 and y < 0:
    print(f"Point ({x}, {y}) is in Quadrant III")
elif x > 0 and y < 0:
    print(f"Point ({x}, {y}) is in Quadrant IV")
elif x == 0 or y == 0:
    print(f"Point ({x}, {y}) is on an axis")
