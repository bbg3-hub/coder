n = int(input("Enter a decimal number: "))

binary = bin(n)[2:]

print(f"Decimal {n} in binary: {binary}")

temp = n
manual_binary = ""

if n == 0:
    manual_binary = "0"
else:
    while temp > 0:
        manual_binary = str(temp % 2) + manual_binary
        temp //= 2

print(f"Manual conversion: {manual_binary}")
