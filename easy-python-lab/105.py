n = int(input("Enter number of rows (half): "))

print("Number diamond:")
for i in range(1, n + 1):
    sequence = list(range(1, i + 1)) + list(range(i - 1, 0, -1))
    spaces = n - i
    print(' ' * spaces + ' '.join(map(str, sequence)))

for i in range(n - 1, 0, -1):
    sequence = list(range(1, i + 1)) + list(range(i - 1, 0, -1))
    spaces = n - i
    print(' ' * spaces + ' '.join(map(str, sequence)))
