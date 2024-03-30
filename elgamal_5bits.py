# Implementation for Elgamanl Cryptographic - 5bits

import random

# Extended Euclidean Algorithm for finding modular inverse
def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return (gcd, y - (b // a) * x, x)

# Modular Inverse
def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

# Fast modular exponentiation
def fast_mod_exp(base, exponent, mod):
    result = 1
    base = base % mod
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % mod
        exponent = exponent // 2
        base = (base * base) % mod
    return result

# Generate large prime number
def generate_prime():
    # A simple method to generate a prime number for educational purpose
    while True:
        p = random.randint(2**4, 2**5)  # 5-bit prime
        if all(p % i != 0 for i in range(2, int(p**0.5) + 1)):
            return p

# Key generation
def generate_keys():
    p = generate_prime()
    g = random.randint(2, p - 1)  # Generator
    x = random.randint(1, p - 2)   # Private key
    y = fast_mod_exp(g, x, p)      # Public key
    return (p, g, y), x

# Encryption
def encrypt(plaintext, public_key):
    p, g, y = public_key
    k = random.randint(1, p - 2)
    c1 = fast_mod_exp(g, k, p)
    c2 = (fast_mod_exp(y, k, p) * plaintext) % p
    return c1, c2

# Decryption
def decrypt(ciphertext, private_key, public_key):
    p, _, _ = public_key
    x = private_key
    c1, c2 = ciphertext
    s = fast_mod_exp(c1, x, p)
    plaintext = (c2 * mod_inverse(s, p)) % p
    return plaintext

# Test the ElGamal encryption and decryption
def test_elgamal():
    # Generate keys
    public_key, private_key = generate_keys()
    print("Public Key (p, g, y):", public_key)
    print("Private Key (x):", private_key)

    # Message to encrypt (5-bit)
    plaintext = random.randint(0, 2**5 - 1)
    print("Plaintext (m):", plaintext)

    # Encrypt the message
    ciphertext = encrypt(plaintext, public_key)
    print("Ciphertext (c1, c2):", ciphertext)

    # Decrypt the ciphertext
    decrypted_plaintext = decrypt(ciphertext, private_key, public_key)
    print("Decrypted Plaintext (m):", decrypted_plaintext)

    # Verify if decryption is successful
    if plaintext == decrypted_plaintext:
        print("Decryption successful!")
    else:
        print("Decryption failed!")

# Run the test
test_elgamal()
