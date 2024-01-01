from cryptography.fernet import Fernet

with open('key.key', 'rb') as key_file:
    key = key_file.read()

cipher_suite = Fernet(key)

with open('encrypted.txt', 'rb') as encrypted_file:
    encrypted_text = encrypted_file.read()

decrypted_text = cipher_suite.decrypt(encrypted_text)

with open('decrypted.txt', 'wb') as decrypted_file:
    decrypted_file.write(decrypted_text)
