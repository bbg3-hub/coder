# Problem 109: X pattern

n = int(input("Enter size: "))

print("X pattern:")
for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
