# Problem 52: Happy Number - repeatedly replace with sum of squares of digits
# A happy number eventually reaches 1; unhappy numbers cycle

def is_happy(n):
    seen = set()
    
    while n != 1 and n not in seen:
        seen.add(n)
        sum_of_squares = 0
        
        while n > 0:
            digit = n % 10
            sum_of_squares += digit * digit
            n //= 10
        
        n = sum_of_squares
    
    return n == 1

n = int(input("Enter a number: "))

if is_happy(n):
    print(f"{n} is a happy number")
else:
    print(f"{n} is not a happy number")
