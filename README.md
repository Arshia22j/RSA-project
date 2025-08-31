# RSA Encryption and Decryption

A simple Python implementation of the **RSA algorithm** for generating public and private keys, encrypting messages, and decrypting them back to plaintext.

---

## 📌 Features

* Generate **public** and **private RSA keys**.
* Encrypt any plaintext message using the public key.
* Decrypt ciphertext using the private key.
* Simple, beginner-friendly implementation with detailed comments.

---

## 📜 How RSA Works

RSA is an **asymmetric encryption algorithm** based on the mathematical difficulty of factoring large prime numbers.

**Steps Involved:**

1. Choose two large prime numbers `p` and `q`.
2. Compute `n = p * q`.
3. Calculate Euler's totient `φ = (p - 1)(q - 1)`.
4. Choose a public exponent `e` such that `gcd(e, φ) = 1`.
5. Calculate the private exponent `d` as the modular inverse of `e` modulo `φ`.
6. **Public Key** = `(e, n)`
7. **Private Key** = `(d, n)`

**Encryption Formula:**

```math
C = (M^e) mod n
```

**Decryption Formula:**

```math
M = (C^d) mod n
```

---

## 🚀 Installation

Clone the repository and navigate into the project folder:

```bash
git clone https://github.com/Arshia22j/RSA-Encryption.git
cd RSA-Encryption
```

(Optional) Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # For Linux & Mac
venv\Scripts\activate      # For Windows
```

Install dependencies (if any):

```bash
pip install -r requirements.txt
```

---

## 🛠️ Usage

Run the Python script:

```bash
python src/rsa_encryption.py
```

Example session:

```
Public Key: (313, 32321)
Private Key: (2017, 32321)

Enter the message to encrypt: Hello RSA
Encrypted Message: [311, 1902, 2921, 2921, 4023, 391]
Decrypted Message: Hello RSA
```

---

## 📂 Project Structure

```
RSA-Encryption/
│── src/
│   └── rsa_encryption.py       # Main Python script
│── examples/
│   └── sample_output.png      # Sample output screenshot
│── README.md
│── requirements.txt
│── LICENSE (optional)
```

---

## 📸 Sample Output

![Sample Output](examples/sample_output.png)

---

## 📄 License

This project is licensed under the **MIT License**. Feel free to use, modify, and distribute.

---

## 🤝 Contributing

Pull requests are welcome! If you find bugs or want to improve the project, feel free to contribute.

---

## ✨ Author

**Arshia J**
GitHub: [Arshia22j](https://github.com/Arshia22j)
Email: [arshia4321.jamalian@gmail.com](mailto:arshia4321.jamalian@gmail.com)

