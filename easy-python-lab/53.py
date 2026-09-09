# Problem 53: Product of Digits - Find using recursion

def product_of_digits(n):
    if n < 10:
        return n
    else:
        return (n % 10) * product_of_digits(n // 10)

n = int(input("Enter a number: "))

result = product_of_digits(abs(n))
print(f"Product of digits of {n}: {result}")
