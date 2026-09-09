# Problem 42: Scholarship Eligibility - based on marks, attendance, and family income

marks = float(input("Enter marks (0-100): "))
attendance = float(input("Enter attendance percentage (0-100): "))
income = float(input("Enter family income (in rupees): "))

if marks >= 80 and attendance >= 75 and income < 500000:
    print("Eligible for scholarship")
elif marks >= 70 and attendance >= 70 and income < 300000:
    print("Eligible for partial scholarship")
else:
    print("Not eligible for scholarship")
