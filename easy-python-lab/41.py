# Problem 41: Given hour and minute, calculate the smaller angle between clock hands

hour = int(input("Enter hour (0-23): "))
minute = int(input("Enter minute (0-59): "))

# Convert to 12-hour format
hour = hour % 12

# Calculate angles
minute_angle = minute * 6  # Each minute is 6 degrees
hour_angle = (hour * 30) + (minute * 0.5)  # Each hour is 30 degrees + minute contribution

# Find the difference
angle_diff = abs(hour_angle - minute_angle)

# Get the smaller angle
smaller_angle = min(angle_diff, 360 - angle_diff)

print(f"Angle between clock hands: {smaller_angle:.2f} degrees")
