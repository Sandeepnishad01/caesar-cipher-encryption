def shift_character(char, shift):
    if char.isalpha():
        shift %= 26
        base = ord('a') if char.islower() else ord('A')
        return chr((ord(char) - base + shift) % 26 + base)
    return char

def encrypt_message(msg, shift_value):
    return ''.join(shift_character(c, shift_value) for c in msg)

def decrypt_message(cipher_text, shift_value):
    return encrypt_message(cipher_text, -shift_value)

def get_user_input(prompt, valid_choices=None):
    while True:
        user_input = input(prompt).lower()
        if not valid_choices or user_input in valid_choices:
            return user_input
        print(f"Invalid choice, please enter one of {valid_choices}.")

def get_shift_value(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid shift value, please enter an integer.")

def main():
    while True:
        action = get_user_input("Would you like to (e)ncrypt or (d)ecrypt a message? Enter 'e' or 'd': ", ['e', 'd'])
        text = input("Enter the message: ")
        shift = get_shift_value("Enter the shift value: ")

        if action == 'e':
            result = encrypt_message(text, shift)
            print("Encrypted message:", result)
        else:
            result = decrypt_message(text, shift)
            print("Decrypted message:", result)
        
        continue_choice = get_user_input("Would you like to encrypt/decrypt another message? (y/n): ", ['y', 'n'])
        if continue_choice != 'y':
            break

if __name__ == "__main__":
    main()