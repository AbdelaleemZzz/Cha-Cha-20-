from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
from cryptography.hazmat.backends import default_backend
import os
import time

key = os.urandom(32)
nonce = os.urandom(16)

with open("testing_file.txt", "rb") as f:
    plaintext = f.read()

start = time.time()
algorithm = algorithms.ChaCha20(key, nonce)
cipher = Cipher(algorithm, mode=None, backend=default_backend())
encryptor = cipher.encryptor()
ciphertext = encryptor.update(plaintext)
end = time.time()

with open("encrypted_crypto.bin", "wb") as f:
    f.write(ciphertext)

print("Cencryption completed.")
print(f"Time taken: {(end - start) * 1000:.4f} ms")
