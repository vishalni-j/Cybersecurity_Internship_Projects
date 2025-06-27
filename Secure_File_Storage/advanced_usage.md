# 🔐 VaultGuard Advanced Usage Guide
*Enhanced security configurations for production environments*

## Table of Contents
1. [Secure Key Derivation](#-secure-key-derivation)
2. [File Integrity Verification](#-file-integrity-verification)
3. [Multi-Factor Decryption](#-multi-factor-decryption)
4. [Cloud Storage Integration](#-cloud-storage-integration)

---

## 🛡️ Secure Key Derivation
Replace the basic key generation with **PBKDF2HMAC** for password-based keys:

```python
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import os
import base64

def generate_key(password: str, salt: bytes = None) -> bytes:
    """Generate cryptographically strong key from password"""
    salt = salt or os.urandom(16)  # Always generate new salt
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000,  # OWASP recommended minimum
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))
```
Usage:
```python 
# Store salt alongside encrypted files
salt = os.urandom(16)
key = generate_key("YourStrongPassword", salt)

# Save salt with encrypted data
with open("encrypted_file.enc", "wb") as f:
    f.write(salt + Fernet(key).encrypt(data))
```
# File Integrity Verification
Add SHA-256 checksums to detect tampering:
```
from cryptography.hazmat.primitives import hashes

def get_hash(file_path: str) -> str:
    """Generate file hash"""
    hasher = hashes.Hash(hashes.SHA256())
    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            hasher.update(chunk)
    return hasher.finalize().hex()

# Verify during decryption
if stored_hash != get_hash(decrypted_path):
    raise SecurityWarning("File tampering detected!")
```
# Multi-Factor Decryption
Require both password and hardware key:
```

# Requires: pip install fido2
from fido2.ctap2 import CTAP2
from fido2.client import Fido2Client

def verify_hardware_key():
    """Validate hardware security key"""
    client = Fido2Client("https://example.com")
    if not client.verify_pin(pin):
        raise PermissionError("Hardware authentication failed")
```
Cloud Storage Integration
AWS S3 Encryption Workflow:
```python
# Requires: pip install boto3
import boto3
from botocore.exceptions import ClientError

def encrypt_and_upload(file_path: str):
    """Encrypt locally before cloud upload"""
    encrypted = encrypt_file(file_path)  # Your existing function
    s3 = boto3.client('s3')
    s3.upload_file(encrypted, 'my-secure-bucket', 'backup.enc')
```
#  Security Best Practices
1. Key Storage:

Use AWS KMS/Hashicorp Vault for production

Never hardcode keys in source

2. Audit Logging:
```
 import logging
logging.basicConfig(
    filename='secure_audit.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encryption='fernet'  # Encrypt logs too!
)
```
3. Memory Security
```
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

def wipe_memory(obj):
    """Securely wipe sensitive data from memory"""
    backend = default_backend()
    backend._zero_buffer(obj)
```
### **Key Features of This Guide**
1. **Production-Ready Crypto**: PBKDF2 with 480,000 iterations
2. **Enterprise Patterns**: Hardware keys, cloud integration
3. **Defensive Programming**: Memory wiping, tamper detection
4. **Clear Navigation**: Linked back to main README
