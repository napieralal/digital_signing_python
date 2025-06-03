# 🔐 RSA Signature Tool (with TRNG + SHAKE256)

This project provides a minimal command-line toolkit for:

- Generating deterministic RSA key pairs using custom entropy (e.g. from a TRNG)
- Digitally signing files using RSA + SHA3-256
- Verifying signatures using a public key

The project uses `pycryptodome` and is built for educational or cryptographic experiments.

---

## 📦 Requirements

- Python 3.7+
- `pycryptodome` library

Install dependencies:

```bash
pip install pycryptodome


rsa-signature-tool/
├── generate_keys.py       # Generate RSA key pair from entropy
├── sign_file.py           # Digitally sign a file
├── verify_signature.py    # Verify a signature
├── seed.bin               # Entropy file (from TRNG or /dev/random)
├── rsa_private.pem        # Generated private RSA key
├── rsa_public.pem         # Generated public RSA key
├── data.txt               # Example file to sign
├── signature.bin          # Output signature


python generate_keys.py

python sign_file.py

python verify_signature.py

