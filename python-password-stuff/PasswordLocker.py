# Description: This program will store a password in an encrypted file. 
# There is also a decryption program that will decrypt the password and print it to the screen. PasswordLocker.py 
# Please install the cryptography and Fernet modules before running this program.
# pip install cryptography
# pip install Fernet




import getpass
from cryptography.fernet import Fernet

# Generate encryption key
key = Fernet.generate_key()
fernet = Fernet(key)

# Prompt user for password and encrypt it
password = getpass.getpass("Enter password: ")
encrypted_password = fernet.encrypt(password.encode())

# Write encrypted password to file
with open("password.txt", "wb") as file:
    file.write(encrypted_password)

# Write encryption key to file
with open("key.txt", "wb") as file:
    file.write(key)

print("Password stored successfully.")