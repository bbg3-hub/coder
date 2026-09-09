n = int(input("Enter number of rows: "))

print("Number pyramid (centered):")
for i in range(1, n + 1):
    numbers = ' '.join(str(j) for j in range(1, i + 1))
    spaces = ' ' * (n - i)
    print(spaces + numbers)
