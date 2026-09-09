n = int(input("Enter size: "))

print("Hollow diamond inside rectangle:")
for i in range(n):
    for j in range(n):
        dist = min(i, j, n - 1 - i, n - 1 - j)
        diamond_pos = abs((n // 2) - i) + abs((n // 2) - j)
        
        if dist == 0 or diamond_pos == n // 2:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
