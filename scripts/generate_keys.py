from cryptography.fernet import Fernet


def genKey():
    key = Fernet.generate_key()

    with open("key", "wb") as f:
        f.write(key)

    return key
