# Problem 83: Inverted pyramid

n = int(input("Enter number of rows: "))

print("Inverted pyramid:")
for i in range(n, 0, -1):
    stars = 2 * i - 1
    spaces = (2 * n - 1 - stars) // 2
    print(' ' * spaces + '*' * stars)
