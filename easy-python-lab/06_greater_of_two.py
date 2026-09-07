a, b = map(int, input("Enter two numbers: ").split())
if a > b:
    print(f"{a} is greater")
elif b > a:
    print(f"{b} is greater")
else:
    print("Both are equal")
