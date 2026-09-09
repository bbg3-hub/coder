# Problem 103: Butterfly pattern

n = int(input("Enter number of rows (half): "))

print("Butterfly pattern:")
# Upper half
for i in range(1, n + 1):
    # Left wing
    for j in range(i):
        print('*', end='')
    # Middle spaces
    spaces = 2 * (n - i)
    print(' ' * spaces, end='')
    # Right wing
    for j in range(i):
        print('*', end='')
    print()

# Lower half
for i in range(n, 0, -1):
    # Left wing
    for j in range(i):
        print('*', end='')
    # Middle spaces
    spaces = 2 * (n - i)
    print(' ' * spaces, end='')
    # Right wing
    for j in range(i):
        print('*', end='')
    print()
