import struct

def rotate_left(value, shift):
    """Performs a left rotation on a 32-bit integer."""
    return ((value << shift) & 0xffffffff) | (value >> (32 - shift))

def quarter_round(a, b, c, d):
    """Core quarter round function as defined in ChaCha20."""
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
    """Generates one ChaCha20 block (512 bits = 64 bytes)."""
    constants = [0x61707865, 0x3320646e, 0x79622d32, 0x6b206574]  # "expand 32-byte k"

    key_words = list(struct.unpack('<8L', key))  # 256-bit key → 8 words
    counter_nonce = [counter] + list(struct.unpack('<3L', nonce))

    state = constants + key_words + counter_nonce
    working_state = state.copy()

    # 20 rounds = 10 double rounds
    for _ in range(10):
        # Column rounds
        working_state[0], working_state[4], working_state[8], working_state[12] = quarter_round(
            working_state[0], working_state[4], working_state[8], working_state[12])
        working_state[1], working_state[5], working_state[9], working_state[13] = quarter_round(
            working_state[1], working_state[5], working_state[9], working_state[13])
        working_state[2], working_state[6], working_state[10], working_state[14] = quarter_round(
            working_state[2], working_state[6], working_state[10], working_state[14])
        working_state[3], working_state[7], working_state[11], working_state[15] = quarter_round(
            working_state[3], working_state[7], working_state[11], working_state[15])

        # Diagonal rounds
        working_state[0], working_state[5], working_state[10], working_state[15] = quarter_round(
            working_state[0], working_state[5], working_state[10], working_state[15])
        working_state[1], working_state[6], working_state[11], working_state[12] = quarter_round(
            working_state[1], working_state[6], working_state[11], working_state[12])
        working_state[2], working_state[7], working_state[8], working_state[13] = quarter_round(
            working_state[2], working_state[7], working_state[8], working_state[13])
        working_state[3], working_state[4], working_state[9], working_state[14] = quarter_round(
            working_state[3], working_state[4], working_state[9], working_state[14])

    # Add original state
    result = [(working_state[i] + state[i]) & 0xffffffff for i in range(16)]
    return struct.pack('<16L', *result)  # Return 64 bytes

def chacha20_encrypt(key, nonce, counter, plaintext):
    """Encrypts the plaintext using ChaCha20."""
    assert len(key) == 32
    assert len(nonce) == 12

    keystream = b''
    blocks = (len(plaintext) + 63) // 64

    for i in range(blocks):
        block = chacha20_block(key, counter + i, nonce)
        keystream += block

    return bytes([p ^ k for p, k in zip(plaintext, keystream[:len(plaintext)])])
