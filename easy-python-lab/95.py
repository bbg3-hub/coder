# Problem 95: Column-wise incrementing

n = int(input("Enter number of rows: "))

print("Column-wise incrementing:")
for i in range(1, n + 1):
    print(' '.join(str(j) for j in range(1, i + 1)))
