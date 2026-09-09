n = int(input("Enter number of rows (half): "))

print("Hourglass:")
for i in range(n, 0, -1):
    stars = 2 * i - 1
    spaces = (2 * n - 1 - stars) // 2
    print(' ' * spaces + '*' * stars)

for i in range(2, n + 1):
    stars = 2 * i - 1
    spaces = (2 * n - 1 - stars) // 2
    print(' ' * spaces + '*' * stars)
