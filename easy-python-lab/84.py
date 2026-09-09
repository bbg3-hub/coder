# Problem 84: Diamond shape

n = int(input("Enter number of rows (half): "))

print("Diamond:")
# Upper half
for i in range(1, n + 1):
    stars = 2 * i - 1
    spaces = (2 * n - 1 - stars) // 2
    print(' ' * spaces + '*' * stars)

# Lower half
for i in range(n - 1, 0, -1):
    stars = 2 * i - 1
    spaces = (2 * n - 1 - stars) // 2
    print(' ' * spaces + '*' * stars)
