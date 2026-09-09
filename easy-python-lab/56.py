# Problem 56: Check if a number is prime

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

n = int(input("Enter a number: "))

if is_prime(n):
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")
