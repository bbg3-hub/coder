# Problem 72: Convert binary to decimal

binary = input("Enter a binary number: ")

decimal = int(binary, 2)

print(f"Binary {binary} in decimal: {decimal}")

# Manual conversion
manual_decimal = 0
for i, bit in enumerate(reversed(binary)):
    manual_decimal += int(bit) * (2 ** i)

print(f"Manual conversion: {manual_decimal}")
