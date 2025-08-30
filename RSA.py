import random

# Function to calculate the Greatest Common Divisor (GCD)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to calculate the modular multiplicative inverse of e mod phi
def mod_inverse(e, phi):
    d = 0
    x1, x2, y1 = 0, 1, 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2, x1 = x1, x
        d, y1 = y1, y

    # Ensure positive value for d
    if temp_phi == 1:
        return d + phi

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to generate a random prime number in a given range
def generate_prime(start, end):
    while True:
        num = random.randint(start, end)
        if is_prime(num):
            return num

# Function to generate RSA public and private keys
def generate_keys():
    # Generate two large prime numbers
    p = generate_prime(100, 300)
    q = generate_prime(100, 300)
    while p == q:
        q = generate_prime(100, 300)

    # Calculate n = p * q
    n = p * q

    # Calculate Euler's totient function phi
    phi = (p - 1) * (q - 1)

    # Choose a random e such that gcd(e, phi) = 1
    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    # Calculate private key exponent d
    d = mod_inverse(e, phi)

    # Return public and private keys
    return ((e, n), (d, n))

# Function to encrypt a plaintext message using the public key
def encrypt(public_key, plaintext):
    e, n = public_key
    # Convert each character to its Unicode code point and apply RSA formula
    cipher = [(ord(char) ** e) % n for char in plaintext]
    return cipher

# Function to decrypt ciphertext using the private key
def decrypt(private_key, ciphertext):
    d, n = private_key
    # Convert each cipher number back to its character representation
    plain = [chr((char ** d) % n) for char in ciphertext]
    return ''.join(plain)

# Main program execution
if __name__ == '__main__':
    # Generate RSA keys
    public_key, private_key = generate_keys()
    print("Public Key:", public_key)
    print("Private Key:", private_key)

    # Take input message from the user
    message = input("Enter the message to encrypt: ")

    # Encrypt the message
    encrypted_msg = encrypt(public_key, message)
    print("Encrypted Message:", encrypted_msg)

    # Decrypt the message
    decrypted_msg = decrypt(private_key, encrypted_msg)
    print("Decrypted Message:", decrypted_msg)
