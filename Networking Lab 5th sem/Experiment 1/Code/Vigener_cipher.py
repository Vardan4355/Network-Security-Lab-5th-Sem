from itertools import cycle


def clean_key(key):
    key = "".join(letter.upper() for letter in key if letter.isalpha())

    if not key:
        raise ValueError("The key must contain at least one letter.")

    return key


def vigenere_cipher(text, key, decrypt=False):
    key = clean_key(key)
    key_stream = cycle(key)
    result = []

    for char in text:
        if char.isalpha():
            key_char = next(key_stream)
            shift = ord(key_char) - ord("A")

            if decrypt:
                shift = -shift

            start = ord("A") if char.isupper() else ord("a")
            new_char = chr((ord(char) - start + shift) % 26 + start)

            result.append(new_char)
        else:
            result.append(char)

    return "".join(result)


def encrypt(text, key):
    return vigenere_cipher(text, key)


def decrypt(text, key):
    return vigenere_cipher(text, key, decrypt=True)


if __name__ == "__main__":
    plaintext = input("Enter the plaintext: ")
    key = input("Enter the key: ")

    ciphertext = encrypt(plaintext, key)
    original_text = decrypt(ciphertext, key)

    print("Encrypted:", ciphertext)
    print("Decrypted:", original_text)
