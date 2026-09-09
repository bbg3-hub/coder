n = int(input("Enter number of rows: "))

print("Alphabet pyramid (centered):")
for i in range(n):
    sequence = []
    for j in range(i + 1):
        sequence.append(chr(ord('A') + j))
    for j in range(i - 1, -1, -1):
        sequence.append(chr(ord('A') + j))
    
    width = 2 * n - 1
    line = ' '.join(sequence)
    spaces = (width * 2 - len(line)) // 2
    print(' ' * spaces + line)
