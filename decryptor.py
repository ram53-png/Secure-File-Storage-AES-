from cryptography.fernet import Fernet
import hashlib

def get_hash(file_path):
    with open(file_path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

with open("secret.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)

with open("encrypted_files/yourfile.txt.enc", "rb") as enc_file:
    encrypted = enc_file.read()

decrypted = fernet.decrypt(encrypted)

# Save decrypted file
with open("decrypted_files/yourfile.txt", "wb") as dec_file:
    dec_file.write(decrypted)

# Verify hash
decrypted_hash = get_hash("decrypted_files/yourfile.txt")
with open("yourfile.hash", "r") as hash_file:
    original_hash = hash_file.read()

if decrypted_hash == original_hash:
    print("✅ Decryption successful and file integrity verified.")
else:
    print("⚠️ Decryption completed, but file integrity check failed.")
