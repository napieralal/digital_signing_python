# 🔐 RSA Signature Tool (with TRNG + SHAKE256)

This project provides a minimal command-line toolkit for:

-   Generating deterministic RSA key pairs using custom entropy (e.g. from a TRNG)
-   Digitally signing files using RSA + SHA3-256
-   Verifying signatures using a public key

The project uses `pycryptodome` and is built for educational or cryptographic experiments.

---

## 📦 Requirements

-   Python 3.7+
-   `pycryptodome` library

## Install dependencies:

```bash
pip install pycryptodome
```

## Project Structure
```
rsa-signature-tool/
├── signature.py       # Generate RSA key pair from entropy
├── sign.py           # Digitally sign a file
├── verify.py    # Verify a signature
├── seed.bin               # Entropy file
├── rsa_private.pem        # Generated private RSA key
├── rsa_public.pem         # Generated public RSA key
├── data.txt               # Example file to sign
├── signature.bin          # Output signature
```

### Generate RSA Keys
```bash
python generate_keys.py
```

### Sign a file
```bash
python sign_file.py
```

### Verify a signature
```bash
python verify_signature.py
```
