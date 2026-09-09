n = int(input("Enter number of rows: "))

print("Sequential number triangle:")
count = 1
for i in range(1, n + 1):
    for j in range(i):
        print(count, end=' ')
        count += 1
    print()
