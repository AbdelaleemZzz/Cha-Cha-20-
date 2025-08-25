import struct
import time

def rotate_left(value, shift):
    return ((value << shift) & 0xffffffff) | (value >> (32 - shift))

def quarter_round(a, b, c, d):
    a = (a + b) & 0xffffffff
    d ^= a
    d = rotate_left(d, 16)
    c = (c + d) & 0xffffffff
    b ^= c
    b = rotate_left(b, 12)
    a = (a + b) & 0xffffffff
    d ^= a
    d = rotate_left(d, 8)
    c = (c + d) & 0xffffffff
    b ^= c
    b = rotate_left(b, 7)
    return a, b, c, d

def chacha20_block(key, counter, nonce):
    constants = [0x61707865, 0x3320646e, 0x79622d32, 0x6b206574]
    key_words = list(struct.unpack('<8L', key))
    counter_nonce = [counter] + list(struct.unpack('<3L', nonce))
    state = constants + key_words + counter_nonce
    working_state = state.copy()

    for _ in range(10):
        working_state[0], working_state[4], working_state[8], working_state[12] = quarter_round(working_state[0], working_state[4], working_state[8], working_state[12])
        working_state[1], working_state[5], working_state[9], working_state[13] = quarter_round(working_state[1], working_state[5], working_state[9], working_state[13])
        working_state[2], working_state[6], working_state[10], working_state[14] = quarter_round(working_state[2], working_state[6], working_state[10], working_state[14])
        working_state[3], working_state[7], working_state[11], working_state[15] = quarter_round(working_state[3], working_state[7], working_state[11], working_state[15])
        working_state[0], working_state[5], working_state[10], working_state[15] = quarter_round(working_state[0], working_state[5], working_state[10], working_state[15])
        working_state[1], working_state[6], working_state[11], working_state[12] = quarter_round(working_state[1], working_state[6], working_state[11], working_state[12])
        working_state[2], working_state[7], working_state[8], working_state[13] = quarter_round(working_state[2], working_state[7], working_state[8], working_state[13])
        working_state[3], working_state[4], working_state[9], working_state[14] = quarter_round(working_state[3], working_state[4], working_state[9], working_state[14])

    result = [(working_state[i] + state[i]) & 0xffffffff for i in range(16)]
    return struct.pack('<16L', *result)

def chacha20_encrypt(key, nonce, counter, plaintext):
    assert len(key) == 32
    assert len(nonce) == 12
    keystream = b''
    blocks = (len(plaintext) + 63) // 64
    for i in range(blocks):
        block = chacha20_block(key, counter + i, nonce)
        keystream += block
    return bytes([p ^ k for p, k in zip(plaintext, keystream[:len(plaintext)])])

# === File-based encryption ===
if __name__ == "__main__":
    key = bytes.fromhex("000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f")
    nonce = bytes.fromhex("000000000000004a00000000")
    counter = 1

    with open("testing_file.txt", "rb") as f:
        plaintext = f.read()

    start = time.time()
    ciphertext = chacha20_encrypt(key, nonce, counter, plaintext)
    end = time.time()

    with open("encrypted_manual_output.bin", "wb") as f:
        f.write(ciphertext)

    print("0encryption completed.")
    print(f"Time taken: {(end - start) * 1000:.2f} ms")
