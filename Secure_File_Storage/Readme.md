## Secure File Storage

# 🔒 VaultGuard - AES-256 File Encryption System

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Cryptography](https://img.shields.io/badge/AES-256_Military_Grade-brightgreen)
![License](https://img.shields.io/badge/License-MIT-red)

A secure file encryption/decryption tool using **AES-256** (Fernet implementation) with built-in auditing.

## 🌟 Key Features
- **Military-grade encryption**: AES-256 algorithm
- **Key management**: Auto-generates and stores `secret.key`
- **Tamper-proof logs**: All operations recorded in `file_encryptor.log`
- **Cross-platform**: Works on Windows, Linux, and macOS

## 🛠️ Installation
```bash
# Clone the repository
git clone https://github.com/your-username/Cybersecurity-Internship-Projects.git
cd Secure_File_Storage

# Install dependencies
pip install cryptography
```
# Usage
Encrypt a file
```bash
python secure_storage.py --encrypt secret_document.txt
```

Outputs:

secret_document.txt.enc (encrypted file)

Log entry: [2024-06-20 14:00] ENCRYPT: secret_document.txt → secret_document.txt.enc

Decrypt a File
```bash
python secure_storage.py --decrypt secret_document.txt.enc
```

Outputs:

Original secret_document.txt

Log entry: [2024-06-20 14:02] DECRYPT: secret_document.txt.enc → secret_document.txt

# File Structure:

 Secure_File_Storage/
├── secure_storage.py      # Main application
├── secret.key            # Auto-generated encryption key (Encrypted)
├── file_encryptor.log    # Operation audit log
└── requirements.txt      # Dependencies

# Security Notes
Backup secret.key: Losing this means losing access to encrypted files

Never commit secret.key: Add to .gitignore

Password-protect keys: For production, use PBKDF2HMAC

# Future Enhancements
Add GUI (Tkinter/PyQt)

Cloud storage integration

File shredding (secure deletion)

# Author

Vishalni J
