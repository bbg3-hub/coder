# Problem 44: Print numbers from N to 1

n = int(input("Enter N: "))

print("Numbers from", n, "to 1")
for i in range(n, 0, -1):
    print(i, end=" ")
print()
