hour = int(input("Enter hour (0-23): "))
minute = int(input("Enter minute (0-59): "))

hour = hour % 12

minute_angle = minute * 6
hour_angle = (hour * 30) + (minute * 0.5)

angle_diff = abs(hour_angle - minute_angle)

smaller_angle = min(angle_diff, 360 - angle_diff)

print(f"Angle between clock hands: {smaller_angle:.2f} degrees")
