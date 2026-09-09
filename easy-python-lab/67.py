n = int(input("Enter a number: "))

digits = [int(d) for d in str(abs(n))]
num_digits = len(digits)

sum_of_powers = sum(d ** num_digits for d in digits)

if sum_of_powers == abs(n):
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number")
