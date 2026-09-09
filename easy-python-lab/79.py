# Problem 79: Inverted right-angled triangle

n = int(input("Enter number of rows: "))

print("Inverted right-angled triangle:")
for i in range(n, 0, -1):
    print('*' * i)
