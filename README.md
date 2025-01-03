## sm-Password-Strength-Checker

### Project Description

sm-Password-Strength-Checker is a robust tool designed to evaluate the strength of passwords against a customizable set of criteria. It empowers organizations to implement stringent password policies, ensuring the security and integrity of their systems. This tool is particularly valuable for managing secrets, such as API keys, passwords, and certificates, which are crucial for maintaining data confidentiality and access control.

### Installation Requirements

- Python 3.6 or later
- Vault (Optional, for advanced functionality)

### Installation Instructions

```
git clone https://github.com/ShadowStrikeHQ/sm-Password-Strength-Checker.git
cd sm-Password-Strength-Checker
pip install -r requirements.txt
```

### Usage Examples

**Basic Usage:**

```
python main.py -p "Password123"
```

**Customized Criteria:**

```
python main.py -p "V3ryStr0ngP@ssw0rd!" -l 16 -u 2 -d 3 -s 4
```

- ```-l 16```: Minimum password length (default: 8)
- ```-u 2```: Minimum number of uppercase characters (default: 1)
- ```-d 3```: Minimum number of digits (default: 1)
- ```-s 4```: Minimum number of special characters (default: 1)

### Security Warnings and Considerations

- This tool is intended for evaluating password strength and should not be used to generate passwords or store them securely.
- Ensure that the tool is run on a secure system with appropriate access controls.

### License Information

This project is licensed under the GNU General Public License v3.0.