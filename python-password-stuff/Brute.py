import itertools
import string
import time

def generate_passwords(length_range=(1, 8)):
    characters = string.ascii_letters + string.digits + string.punctuation
    for length in range(length_range[0], length_range[1] + 1):
        for combination in itertools.product(characters, repeat=length):
            yield ''.join(combination)

def crack_password(target_password):
    start_time = time.time()
    attempts = 0
    
    for guess_password in generate_passwords():
        attempts += 1
        if guess_password == target_password:
            end_time = time.time()
            elapsed_time = end_time - start_time
            return guess_password, attempts, elapsed_time

if __name__ == "__main__":
    user_password = input("Enter the target password: ")

    cracked_password, attempts, elapsed_time = crack_password(user_password)
    
    print("Password cracked!")
    print("Target password:", user_password)
    print("Cracked password:", cracked_password)
    print("Attempts:", attempts)
    print("Time taken (seconds):", elapsed_time)
