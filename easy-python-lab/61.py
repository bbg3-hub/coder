n = int(input("Enter N: "))

sum_reciprocals = 0

for i in range(1, n + 1):
    sum_reciprocals += 1 / i

print(f"Sum of 1 + 1/2 + 1/3 + ... + 1/{n} = {sum_reciprocals:.6f}")
