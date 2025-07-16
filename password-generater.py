import random
import string

def generate_password(length=12):
    if length < 4:
        return "Password length should be at least 4."

    # Character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure at least one character from each category
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols),
    ]

    # Fill the remaining length
    all_chars = lowercase + uppercase + digits + symbols
    password += random.choices(all_chars, k=length - 4)

    # Shuffle to avoid predictable pattern
    random.shuffle(password)

    return ''.join(password)

# Example usage
if __name__ == "__main__":
    user_length = int(input("Enter password length (min 4): "))
    print("Generated Password:", generate_password(user_length))
