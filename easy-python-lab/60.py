# Problem 60: Print Fibonacci series up to N terms

n = int(input("Enter number of terms: "))

if n <= 0:
    print("Please enter a positive number")
elif n == 1:
    print("Fibonacci series: 0")
else:
    fib_series = [0, 1]
    
    for i in range(2, n):
        fib_series.append(fib_series[i-1] + fib_series[i-2])
    
    print(f"Fibonacci series up to {n} terms:")
    print(fib_series[:n])
