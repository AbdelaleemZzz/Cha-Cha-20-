from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
from cryptography.hazmat.backends import default_backend
import os

# Generate key (32 bytes = 256-bit)
key = os.urandom(32)

# Generate nonce (12 bytes)
nonce = os.urandom(16)  # cryptography uses 16-byte nonce for ChaCha20

# Message
plaintext = b"ChaCha20 is cool"

# Encrypt
algorithm = algorithms.ChaCha20(key, nonce)
cipher = Cipher(algorithm, mode=None, backend=default_backend())
encryptor = cipher.encryptor()
ciphertext = encryptor.update(plaintext)

# Decrypt
decryptor = cipher.decryptor()
decrypted = decryptor.update(ciphertext)

# Output
print("Original:  ", plaintext)
print("Encrypted: ", ciphertext.hex())
print("Decrypted: ", decrypted)
