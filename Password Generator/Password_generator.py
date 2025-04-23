import random
import string

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length should be at least 4")

    # Ensure at least one character from each category
    uppercase = random.choice(string.ascii_uppercase)
    lowercase = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special = random.choice(string.punctuation)

    # Fill the rest randomly
    remaining_length = length - 4
    all_chars = string.ascii_letters + string.digits + string.punctuation
    remaining_chars = ''.join(random.choices(all_chars, k=remaining_length))

    # Combine and shuffle
    password = list(uppercase + lowercase + digit + special + remaining_chars)
    random.shuffle(password)

    return ''.join(password)

if __name__ == "__main__":
    print("🔐 Welcome to the Password Generator!")
    while True:
        try:
            length = int(input("Enter desired password length (minimum 4): "))
            print("Generated Password:", generate_password(length))
        except ValueError as ve:
            print("Error:", ve)

        again = input("Do you want to generate another password? (yes/no): ").strip().lower()
        if again != "yes":
            print("Goodbye!")
            break
