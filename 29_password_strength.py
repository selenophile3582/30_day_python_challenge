# 🔥 Q29 – Password Strength Checker

# Take password from user.
# Check if it has:
# Minimum 8 characters
# At least 1 uppercase
# At least 1 lowercase
# At least 1 digit
# At least 1 special character
# Print:
# Strong
# Weak
# 💡 Very practical real-world problem.

password = input("Enter your password : ")

has_special = False
has_digit = False
has_lower = False
has_upper = False
length = len(password)

for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
    elif not ch.isalnum() and not ch.isspace():
        has_special = True  
              
    if has_upper and has_lower and has_digit and has_special and length >= 8:
        print("Strong Password !!")
        break
else :
    print("Weak password !!")