import string


def shift_alphabet(char, shift):
    if char in string.ascii_lowercase:
        alphabet = string.ascii_lowercase
    elif char in string.ascii_uppercase:
        alphabet = string.ascii_uppercase
    else:
        return char

    position = alphabet.index(char)
    new_position = (position + shift) % 26
    return alphabet[new_position]


def encrypt(message, shift):
    return "".join(shift_alphabet(char, shift) for char in message)


def decrypt(message, shift):
    return encrypt(message, -shift)


def main():
    message = input("Enter the message: ")
    shift = int(input("Enter the shift amount: "))

    encrypted_message = encrypt(message, shift)
    decrypted_message = decrypt(encrypted_message, shift)

    print("Encrypted message:", encrypted_message)
    print("Decrypted message:", decrypted_message)


if __name__ == "__main__":
    main()
