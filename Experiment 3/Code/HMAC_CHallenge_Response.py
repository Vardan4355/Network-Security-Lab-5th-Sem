import hashlib
import hmac
import secrets
import time

SECRET_KEY = b"network_security_lab_secret"
CHALLENGE_LIFETIME = 5
USED_NONCES = set()


def create_challenge(username):
    nonce = secrets.token_urlsafe(16)
    issued_at = int(time.time())

    data = f"{username}|{nonce}|{issued_at}".encode()
    signature = hmac.new(
        SECRET_KEY,
        data,
        hashlib.sha256
    ).hexdigest()

    return {
        "username": username,
        "nonce": nonce,
        "issued_at": issued_at,
        "signature": signature
    }


def authenticate(challenge):
    required_fields = ("username", "nonce", "issued_at", "signature")

    if any(field not in challenge for field in required_fields):
        return "Rejected: Missing authentication data."

    username = challenge["username"]
    nonce = challenge["nonce"]
    issued_at = challenge["issued_at"]
    received_signature = challenge["signature"]

    if not isinstance(username, str) or not username:
        return "Rejected: Invalid username."

    if not isinstance(nonce, str) or not nonce:
        return "Rejected: Invalid nonce."

    try:
        issued_at = int(issued_at)
    except (TypeError, ValueError):
        return "Rejected: Invalid timestamp."

    if nonce in USED_NONCES:
        return "Rejected: Replay attack detected."

    current_time = int(time.time())

    if current_time - issued_at > CHALLENGE_LIFETIME:
        return "Rejected: Challenge has expired."

    if issued_at - current_time > CHALLENGE_LIFETIME:
        return "Rejected: Invalid future timestamp."

    data = f"{username}|{nonce}|{issued_at}".encode()
    expected_signature = hmac.new(
        SECRET_KEY,
        data,
        hashlib.sha256
    ).hexdigest()

    if not hmac.compare_digest(received_signature, expected_signature):
        return "Rejected: Invalid authentication signature."

    USED_NONCES.add(nonce)
    return f"Accepted: {username} authenticated successfully."


def main():
    print("=== Challenge-Response Authentication ===")

    valid_challenge = create_challenge("alice")
    print("\n1. Valid challenge:")
    print(authenticate(valid_challenge))

    print("\n2. Replay attempt:")
    print(authenticate(valid_challenge))

    expired_challenge = create_challenge("alice")
    expired_challenge["issued_at"] = int(time.time()) - 20

    print("\n3. Expired challenge:")
    print(authenticate(expired_challenge))

    tampered_challenge = create_challenge("alice")
    tampered_challenge["signature"] = "invalid-signature"

    print("\n4. Tampered signature:")
    print(authenticate(tampered_challenge))


if __name__ == "__main__":
    main()
