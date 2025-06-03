from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA3_256
from Crypto.PublicKey import RSA
import os

data_path = input("File with data [default: data.txt]: ").strip() or "data.txt"
if not os.path.exists(data_path):
    print("Error: file does not exists.")
    exit(1)

sig_path = input("File with signature [default: signature.sig]: ").strip() or "signature.sig"
if not os.path.exists(sig_path):
    print("Error: signature file does not exists.")
    exit(1)

pubkey_path = input("File with public key [default: rsa_public.pem]: ").strip() or "rsa_public.pem"
if not os.path.exists(pubkey_path):
    print("Error: file with public key does not exists.")
    exit(1)

with open(data_path, "rb") as f:
    data = f.read()
with open(sig_path, "rb") as f:
    signature = f.read()
with open(pubkey_path, "rb") as f:
    public_key = RSA.import_key(f.read())

digest = SHA3_256.new(data)

try:
    pkcs1_15.new(public_key).verify(digest, signature)
    print("Signature is correct.")
except (ValueError, TypeError):
    print("Incorrect signature!")
