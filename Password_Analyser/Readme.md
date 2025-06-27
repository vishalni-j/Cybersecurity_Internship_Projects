# 🔐 Password Strength Analyzer & Wordlist Generator    

# 🛡️ Ethical Access OWASP Compliance Security Tool  

## 📌 Summary  
A penetration testing and ethical hacking focused password strength analyser wordlist generator. It implements both auditing algorithms and brute-force simulations alongside the zxcvbn algorithm Your security in mind!  

---  
  
# 💼 Use Cases  

- Audit grade pre-defined scoring system (0–4) with zxcvbn
  
- Common attack scenarios estimate time to breach for users account security

- Custom targeted keyword based yearly wordlist generation 

- Flexibility with a command line interface.

- Tracks usage activity in `password_tool.log`.

---

## 🛠️ Tech Stack

- Python 3.
  
 - Password complexity scoring zxcvbn.  

 - Permutation generators itertools.  

 - CLI argument parsing argparse.  

 - Event logging logging.
 
---

## ⚙️ Steps For Activation
### 🔧 Deployment

```bash

pip install zxcvbn

python password_tool.py --password "P@ssw0rd123!" 
```
# Sample Output 

Score: 2/4 | Crack Time: 3 hours

```bash

python password_tool.py --generate --keywords "admin,user" --years "2020,2025"

```
# Sample Wordlist

admin2020
admin2025
user2020
user2025

# File Structure
├── password_analyzer.py          # Main script
├──  password_tool.log            # Activity log
├──  Wordlist_genearator.py        # Wordlist generating script
├── wordlist.txt                  # Output wordlist
├── README.md                     # Project Documentation

# Ethical Use Disclaimer
This tool is intended strictly for educational purposes and authorized security assessments.

🔒 Do not use this tool on systems or accounts you do not own or have explicit permission to test.

# Future Enhancements
- Add a GUI with Tkinter

- Integrate with Have I Been Pwned API

- Include smart substitutions (e.g., leetspeak)

# Learning Outcomes
- Password entropy and strength evaluation

- Brute-force simulation with custom lists

- Secure coding practices in Python

# Author

Vishalni J





