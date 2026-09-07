hour = int(input("Enter hour (0-23): "))

if hour < 12:
    greeting = "Morning"
elif hour < 18:
    greeting = "Afternoon"
elif hour < 21:
    greeting = "Evening"
else:
    greeting = "Night"

print(f"Hour {hour}: {greeting}")
