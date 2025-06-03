from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA3_256
from Crypto.PublicKey import RSA
import os

data_path = input("File to sign [default: data.txt]: ").strip() or "data.txt"
if not os.path.exists(data_path):
    print("Error: file does not exists.")
    exit(1)

with open(data_path, "rb") as f:
    data = f.read()

with open("rsa_private.pem", "rb") as f:
    private_key = RSA.import_key(f.read())

digest = SHA3_256.new(data)

signature = pkcs1_15.new(private_key).sign(digest)

with open("signature.sig", "wb") as f:
    f.write(signature)

print("File was signed and saved as 'signature.sig'.")
