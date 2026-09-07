age = int(input("Enter customer's age: "))

# Pricing: Child (0-12): $5, Teen (13-19): $8, Adult (20-64): $12, Senior (65+): $7
if age <= 12:
    price = 5
    category = "Child"
elif age <= 19:
    price = 8
    category = "Teen"
elif age <= 64:
    price = 12
    category = "Adult"
else:
    price = 7
    category = "Senior"

print(f"Age: {age}, Category: {category}, Ticket Price: ${price}")
