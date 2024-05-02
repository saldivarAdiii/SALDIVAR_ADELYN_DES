from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

# Generate DES key
def generate_des_key():
    return get_random_bytes(8)

# Encryption function
def encrypt_message(message, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_message = _pad_message(message)
    return cipher.encrypt(padded_message)

# Decryption function
def decrypt_message(encrypted_message, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_message = cipher.decrypt(encrypted_message)
    return _unpad_message(decrypted_message)

def _pad_message(message):
    padding_length = 8 - len(message) % 8
    padding = bytes([padding_length] * padding_length)
    return message + padding

def _unpad_message(message):
    padding_length = message[-1]
    return message[:-padding_length]

if __name__ == "__main__":
    # Generate DES key
    des_key = generate_des_key()
    print("DES Key:", des_key.hex())

    # Encrypt
    plaintext = "Hello, World!"
    encrypted_message = encrypt_message(plaintext.encode(), des_key)
    print("Encrypted Message:", encrypted_message.hex())

    # Decrypt
    decrypted_message = decrypt_message(encrypted_message, des_key)
    print("Decrypted Message:", decrypted_message.decode())
