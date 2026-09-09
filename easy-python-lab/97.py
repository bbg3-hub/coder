n = int(input("Enter number of rows: "))

print("Binary number triangle:")
for i in range(n):
    for j in range(i + 1):
        print((j + i) % 2, end=' ')
    print()
