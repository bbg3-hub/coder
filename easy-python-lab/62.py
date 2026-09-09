n = int(input("Enter number of terms: "))

sum_alternating = 0

for i in range(1, n + 1):
    if i % 2 == 1:
        sum_alternating += i
    else:
        sum_alternating -= i

print(f"Alternating sum up to {n} terms: {sum_alternating}")
