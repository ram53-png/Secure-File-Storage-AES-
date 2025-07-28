from cryptography.fernet import Fernet
import os
import hashlib

def get_hash(file_path):
    with open(file_path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

# Generate & save a key (once)
if not os.path.exists("secret.key"):
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
else:
    with open("secret.key", "rb") as key_file:
        key = key_file.read()

fernet = Fernet(key)

input_file = "sample_files/yourfile.txt"
with open(input_file, "rb") as file:
    original = file.read()

encrypted = fernet.encrypt(original)

# Save encrypted file
with open("encrypted_files/yourfile.txt.enc", "wb") as enc_file:
    enc_file.write(encrypted)

# Save hash
with open("yourfile.hash", "w") as hash_file:
    hash_file.write(get_hash(input_file))

print("✅ File encrypted and saved as yourfile.txt.enc")
