# Problem 45: Print all even numbers from 1 to N

n = int(input("Enter N: "))

print("Even numbers from 1 to", n)
for i in range(2, n + 1, 2):
    print(i, end=" ")
print()
