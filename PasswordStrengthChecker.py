password = input("Enter your password: ")

has_upper = any(char.isupper()for char in password)
has_digit = any(char.isdigit() for char in password)
has_special = any(not char.isalnum() for char in password)

if len(password) < 8:
    print("Password is weak.")

elif has_upper and has_digit and has_special:
        print("Password is strong")

elif has_upper or has_digit or has_special:
        print("Password is medium")

else:    print("Weak Password")

    
