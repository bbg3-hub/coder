units = int(input("Enter units consumed: "))

# Slab rates: 0-100: Rs 5/unit, 101-200: Rs 7/unit, 201-300: Rs 10/unit, >300: Rs 15/unit
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = 100 * 5 + (units - 100) * 7
elif units <= 300:
    bill = 100 * 5 + 100 * 7 + (units - 200) * 10
else:
    bill = 100 * 5 + 100 * 7 + 100 * 10 + (units - 300) * 15

print(f"Units: {units}, Bill: Rs {bill}")
