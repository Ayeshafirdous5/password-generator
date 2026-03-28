import random
import string
import pyperclip


def generate_password(length, use_digits, use_symbols, avoid_similar):
    characters = string.ascii_letters

    # Remove similar looking letters
    if avoid_similar:
        characters = ''.join(c for c in characters if c not in 'OolI')

    if use_digits:
        digits = string.digits
        if avoid_similar:
            digits = ''.join(d for d in digits if d not in '01')
        characters += digits

    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def check_strength(password):
    strength = "Weak"

    if len(password) >= 8:
        strength = "Medium"

    if (len(password) >= 12 and
        any(c.isdigit() for c in password) and
        any(c.isupper() for c in password) and
        any(c in string.punctuation for c in password)):
        strength = "Strong"

    return strength


def main():
    print("🔐 Password Generator\n")

    length = int(input("Enter password length: "))

    use_digits = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    avoid_similar = input("Avoid similar characters (0, O, l, 1)? (y/n): ").lower() == 'y'

    password = generate_password(length, use_digits, use_symbols, avoid_similar)

    print(f"\n✅ Generated Password: {password}")

    strength = check_strength(password)
    print(f"🔎 Strength: {strength}")

    copy = input("Copy to clipboard? (y/n): ").lower()
    if copy == 'y':
        pyperclip.copy(password)
        print("📋 Password copied to clipboard!")


if __name__ == "__main__":
    main()