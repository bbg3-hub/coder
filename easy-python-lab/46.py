# Problem 46: Print all odd numbers from 1 to N

n = int(input("Enter N: "))

print("Odd numbers from 1 to", n)
for i in range(1, n + 1, 2):
    print(i, end=" ")
print()
