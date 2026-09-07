c = input("Enter a character: ")[0]
if "A" <= c <= "Z":
    print("Uppercase letter")
elif "a" <= c <= "z":
    print("Lowercase letter")
elif "0" <= c <= "9":
    print("Digit")
else:
    print("Special character")
