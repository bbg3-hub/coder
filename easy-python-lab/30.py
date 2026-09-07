a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == '+':
    result = a + b
elif operator == '-':
    result = a - b
elif operator == '*':
    result = a * b
elif operator == '/':
    if b != 0:
        result = a / b
    else:
        print("Error: Division by zero")
        exit()
else:
    print("Invalid operator")
    exit()

print(f"{a} {operator} {b} = {result}")
