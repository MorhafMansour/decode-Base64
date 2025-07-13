from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

with open("C:\\the\path\for\encrypted\file"), 'rb') as f:
    content = f.read()
    content_hex = content.hex()

iv = bytes.fromhex(content_hex[:24])
tag = bytes.fromhex(content_hex[-32:])
ciphertext = bytes.fromhex(content_hex[24:-32])

key_hex = "6433616462333366643361646233336664336164623333666433616462333366"
key = bytes.fromhex(key_hex)

cipher = Cipher(
    algorithms.AES(key),
    modes.GCM(iv, tag),
    backend=default_backend()
)
decryptor = cipher.decryptor()
try:
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    print("Decrypted Text:")
    print(plaintext.decode('utf-8', errors='ignore'))
except Exception as e:
    print("Failed to decrypt:", e)
