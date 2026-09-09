# Problem 69: Print all factors / divisors of a number

n = int(input("Enter a number: "))

print(f"Divisors of {n}:")
divisors = []

for i in range(1, abs(n) + 1):
    if n % i == 0:
        divisors.append(i)

print(divisors)
