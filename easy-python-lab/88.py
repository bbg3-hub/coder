n = int(input("Enter number of rows: "))

print("Number triangle (row-wise):")
for i in range(1, n + 1):
    for j in range(i):
        print(i, end=' ')
    print()
