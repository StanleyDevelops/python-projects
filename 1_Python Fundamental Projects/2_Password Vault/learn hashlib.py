# Hashlib for cryptographic hashing
# salting

# Basic hashing with SHA-256
import hashlib

password = "secretpassword123"

# convert string to byte 'cause hashlib works with bytes
password_byte = password.encode("utf-8")

# generate SHA-256 hash
hash_object = hashlib.sha256(password_byte)

# generate hash into readable hexadecimal string
password_hash = hash_object.hexdigest()

print(f"Original Password: {password}")
print(f"SHA-256 Hash: {password_hash}")

print()
