from Crypto.PublicKey import RSA
from Crypto.Hash import SHAKE256
import os

entropy_path = input("File with entropy [default: seed.bin]: ").strip() or "seed.bin"

if not os.path.exists(entropy_path):
    print("Error: file does not exists.")
    exit(1)

with open(entropy_path, "rb") as f:
    entropy = f.read()

shake = SHAKE256.new(data=entropy)

def deterministic_randfunc(n):
    return shake.read(n)

key = RSA.generate(2048, randfunc=deterministic_randfunc)

with open("rsa_private.pem", "wb") as f:
    f.write(key.export_key())

with open("rsa_public.pem", "wb") as f:
    f.write(key.publickey().export_key())

print("Keys were generated and saved.")
