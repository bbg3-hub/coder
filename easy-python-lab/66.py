# Problem 66: Find the sum of even and odd numbers separately from 1 to N

n = int(input("Enter N: "))

sum_even = 0
sum_odd = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i

print(f"Sum of even numbers from 1 to {n}: {sum_even}")
print(f"Sum of odd numbers from 1 to {n}: {sum_odd}")
