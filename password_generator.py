import random
import string

# Generates a random password with letters, digits, and symbols. 

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("=== Password Generator ===")
    try:
        length = int(input("Enter password length: "))
        if length < 6:
            print("Password too short! Using minimum length of 6.")
            length = 6
        password = generate_password(length)
        print(f"Generated password: {password}")
    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":
    main()