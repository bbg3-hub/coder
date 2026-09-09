hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))

if hours <= 40:
    salary = hours * rate
    print(f"Salary: Rs. {salary:.2f}")
else:
    regular_pay = 40 * rate
    overtime_hours = hours - 40
    overtime_pay = overtime_hours * rate * 1.5
    total_salary = regular_pay + overtime_pay
    print(f"Regular pay: Rs. {regular_pay:.2f}")
    print(f"Overtime pay: Rs. {overtime_pay:.2f}")
    print(f"Total salary: Rs. {total_salary:.2f}")
