from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open('key.key', 'wb') as key_file:
    key_file.write(key)

cipher_suite = Fernet(key)

with open('input.txt', 'rb') as file:
    original_text = file.read()

encrypted_text = cipher_suite.encrypt(original_text)

with open('encrypted.txt', 'wb') as encrypted_file:
    encrypted_file.write(encrypted_text)
