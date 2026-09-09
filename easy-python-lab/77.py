def print_numbers(n, current=1, direction="up"):
    if direction == "up":
        if current <= n:
            print(current, end=" ")
            print_numbers(n, current + 1, "up")
        else:
            print()
            print_numbers(n, n - 1, "down")
    else:
        if current >= 1:
            print(current, end=" ")
            print_numbers(n, current - 1, "down")
        else:
            print()

n = int(input("Enter N: "))
print("Increasing then decreasing:")
print_numbers(n)
