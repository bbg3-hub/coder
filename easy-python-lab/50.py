# Problem 50: Reverse a number

n = int(input("Enter a number: "))

reversed_num = 0
temp = abs(n)
original_temp = temp

while temp > 0:
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit
    temp //= 10

if n < 0:
    reversed_num = -reversed_num

print(f"Reverse of {n}: {reversed_num}")
