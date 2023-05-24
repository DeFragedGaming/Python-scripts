def check_password_strength(password):
    # Define the criteria for a strong password
    minimum_length = 8
    requires_uppercase = True
    requires_lowercase = True
    requires_numbers = True
    requires_special_characters = True

    # Check the password length
    if len(password) < minimum_length:
        return "Weak"
    
    # Check for uppercase letters
    if requires_uppercase and not any(char.isupper() for char in password):
        return "Weak"
    
    # Check for lowercase letters
    if requires_lowercase and not any(char.islower() for char in password):
        return "Weak"
    
    # Check for numbers
    if requires_numbers and not any(char.isdigit() for char in password):
        return "Weak"
    
    # Check for special characters
    if requires_special_characters and not any(char in "!@#$%^&*()-_+=[]{}|\\:;'\"<>,.?/~`" for char in password):
        return "Weak"

    return "Strong"

# Prompt the user to enter a password
password = input("Enter a password: ")

# Check the password strength
strength = check_password_strength(password)

# Provide feedback to the user
print("Password strength: " + strength)