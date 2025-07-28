# Secure File Storage with AES Encryption

## Objective:
To securely store and retrieve files using AES-256 encryption with file integrity check.

## Tools Used:
- Python
- Cryptography (Fernet)
- Hashlib (SHA-256)

## How It Works:
- The original file is encrypted using AES and saved with `.enc` extension.
- A hash of the original file is generated and saved to verify integrity.
- Decryption restores the file and verifies it with the saved hash.

## Files Included:
- `encryptor.py` – Encrypts the file and generates hash.
- `decryptor.py` – Decrypts the file and verifies integrity.
- `secret.key` – AES encryption key (generated once).
- `yourfile.hash` – SHA-256 hash of original file.
- Sample folders for original, encrypted, and decrypted files.

## Conclusion:
This project demonstrates how strong encryption and hashing can be used to securely store files and prevent tampering.
