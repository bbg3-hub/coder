n = int(input("Enter number of rows: "))

print("1-0 alternating triangle:")
for i in range(1, n + 1):
    for j in range(i):
        print((j + i) % 2, end=' ')
    print()
