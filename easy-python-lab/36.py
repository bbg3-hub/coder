# Problem 36: Read cost price and selling price - print profit, loss, or no profit no loss

cost_price = float(input("Enter cost price: "))
selling_price = float(input("Enter selling price: "))

difference = selling_price - cost_price

if difference > 0:
    profit_percent = (difference / cost_price) * 100
    print(f"Profit: Rs. {difference:.2f} ({profit_percent:.2f}%)")
elif difference < 0:
    loss_percent = (abs(difference) / cost_price) * 100
    print(f"Loss: Rs. {abs(difference):.2f} ({loss_percent:.2f}%)")
else:
    print("No profit, no loss")
