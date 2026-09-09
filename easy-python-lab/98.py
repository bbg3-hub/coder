# Problem 98: Alphabet triangle (row repeat)

n = int(input("Enter number of rows: "))

print("Alphabet triangle (row repeat):")
for i in range(n):
    char = chr(ord('A') + i)
    print((char + ' ') * (i + 1))
