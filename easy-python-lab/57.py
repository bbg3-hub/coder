# Problem 57: Print all prime numbers from 1 to N

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True

n = int(input("Enter N: "))

primes = []
for i in range(2, n + 1):
    if is_prime(i):
        primes.append(i)

print(f"Prime numbers from 1 to {n}:")
print(primes)
