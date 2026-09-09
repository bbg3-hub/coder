n = int(input("Enter a number: "))

sum_digits = 0
temp = abs(n)

while temp > 0:
    digit = temp % 10
    sum_digits += digit
    temp //= 10

print(f"Sum of digits of {n}: {sum_digits}")
