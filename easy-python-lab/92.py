def binomial_coefficient(n, k):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    
    result = 1
    for i in range(min(k, n - k)):
        result = result * (n - i) // (i + 1)
    return result

n = int(input("Enter number of rows: "))

print("Pascal's triangle:")
for i in range(n):
    for j in range(i + 1):
        print(binomial_coefficient(i, j), end=' ')
    print()
