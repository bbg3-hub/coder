# Problem 32: Check if number is positive, negative, or zero - then if positive check even/odd

n = int(input("Enter a number: "))

if n > 0:
    if n % 2 == 0:
        print(f"{n} is positive and even")
    else:
        print(f"{n} is positive and odd")
elif n < 0:
    print(f"{n} is negative")
else:
    print("Number is zero")
