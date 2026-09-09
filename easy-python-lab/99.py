n = int(input("Enter number of rows: "))

print("Alphabet triangle (sequential):")
for i in range(n):
    for j in range(i + 1):
        print(chr(ord('A') + j), end=' ')
    print()
