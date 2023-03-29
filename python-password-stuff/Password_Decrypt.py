# Password decryption for PasswordLocker.py

import getpass
from cryptography.fernet import Fernet

# Load encryption key
with open("key.txt", "rb") as file:
    key = file.read()

# Load encrypted password
with open("password.txt", "rb") as file:
    encrypted_password = file.read()

# Decrypt password and print it
fernet = Fernet(key)
password = fernet.decrypt(encrypted_password).decode()
print("Password:", password)