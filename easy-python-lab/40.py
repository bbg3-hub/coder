# Problem 40: ATM Withdrawal - Approve/reject based on amount, balance, minimum-balance rules

balance = float(input("Enter current balance: "))
withdrawal_amount = float(input("Enter withdrawal amount: "))
min_balance = 500  # Minimum balance to maintain

if withdrawal_amount <= 0:
    print("Invalid withdrawal amount")
elif withdrawal_amount > balance:
    print(f"Insufficient balance. Current balance: Rs. {balance:.2f}")
elif (balance - withdrawal_amount) < min_balance:
    print(f"Cannot withdraw. Minimum balance of Rs. {min_balance} must be maintained")
else:
    new_balance = balance - withdrawal_amount
    print(f"Withdrawal approved")
    print(f"Amount withdrawn: Rs. {withdrawal_amount:.2f}")
    print(f"Remaining balance: Rs. {new_balance:.2f}")
