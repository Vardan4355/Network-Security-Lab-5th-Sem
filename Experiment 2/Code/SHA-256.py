from pathlib import Path
from hashlib import sha256
import hmac

BASE_DIR = Path(__file__).parent
FILE_PATH = BASE_DIR / "sample.txt"


def calculate_hash(path):
    """Return the SHA-256 hash of a file."""
    digest = sha256()

    with path.open("rb") as file:
        while data := file.read(4096):
            digest.update(data)

    return digest.hexdigest()


def compare_hashes(first_hash, second_hash):
    """Compare two hashes securely."""
    return hmac.compare_digest(first_hash, second_hash)


def count_hash_differences(first_hash, second_hash):
    return sum(
        char1 != char2
        for char1, char2 in zip(first_hash, second_hash)
    )


def main():
    original_text = "Network Security is important in it"

    # Create the original file
    FILE_PATH.write_text(original_text, encoding="utf-8")

    trusted_hash = calculate_hash(FILE_PATH)

    print("Original text:", original_text)
    print("Trusted SHA-256:", trusted_hash)
    print("Initial status: Matched")

    # Modify the file
    changed_text = original_text.replace("important", "Important", 1)
    FILE_PATH.write_text(changed_text, encoding="utf-8")

    current_hash = calculate_hash(FILE_PATH)
    hashes_match = compare_hashes(trusted_hash, current_hash)

    print("\nModified text:", changed_text)
    print("Current SHA-256:", current_hash)
    print("Different hexadecimal characters:",
          count_hash_differences(trusted_hash, current_hash), "/ 64")

    if hashes_match:
        print("Integrity status: Matched")
        print("File integrity verified.")
    else:
        print("Integrity status: Mismatched")
        print("Tampering detected: the file has been changed.")


if __name__ == "__main__":
    main()
