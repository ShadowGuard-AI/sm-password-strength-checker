![Banner](banner.png)

## sm-Password-Strength-Checker

### Project Description

sm-Password-Strength-Checker evaluates one password supplied on the command line against a set of minimum criteria and prints a single verdict. It checks length, uppercase letters, lowercase letters, digits and special characters, and reports only the first criterion the password fails. It does not generate passwords, store passwords, estimate entropy, or check passwords against breach lists.

### Requirements

- Python 3.6 or later
- No third party packages. The tool uses only the standard library, this repository has no requirements.txt, and there is no Vault integration.

### Installation

```
git clone https://github.com/ShadowGuardAI/sm-password-strength-checker.git
cd sm-password-strength-checker
```

### Usage

```
python main.py -p "Password123"
python main.py --password "V3ryStr0ngP@ss!"
python main.py --help
python main.py --version
```

- `-p`, `--password` (required): the password to evaluate.
- `-l`, `--min-length`: minimum password length (default: 8)
- `-u`, `--min-uppercase`: minimum number of uppercase characters (default: 1)
- `-d`, `--min-digits`: minimum number of digits (default: 1)
- `-s`, `--min-special`: minimum number of special characters (default: 1)
- `--version`: print `sm-Password-Strength-Checker 1.0` and exit

At least one lowercase letter is always required and cannot be configured. The special characters recognised are the characters in `!@#$%^&*(),.?":{}|<>`. Minimum length must be at least 1 and the other minimums must be 0 or more; invalid values are rejected with an argparse error and exit status 2. Running without a password also exits with status 2.

### Examples with verified output

Basic usage. `Password123` has no special character, so it fails on that criterion:

```
$ python main.py -p "Password123"
Weak: Password must contain at least one special character.
```

A password that meets the default criteria:

```
$ python main.py --password "V3ryStr0ngP@ss!"
Strong: Your password meets the criteria.
```

Customized criteria:

```
$ python main.py -p "V3ryStr0ngP@ssw0rd!#$" -l 16 -u 2 -d 3 -s 4
Strong: Your password meets the criteria.
```

The same criteria applied to a password with only two special characters:

```
$ python main.py -p "V3ryStr0ngP@ssw0rd!" -l 16 -u 2 -d 3 -s 4
Weak: Password must contain at least 4 special characters.
```

The verdict is printed to stdout. Two informational log lines about the evaluation starting and completing are printed to stderr. The exit status is 0 for both Strong and Weak verdicts.

### Security warnings and considerations

- This tool evaluates password strength only. It does not generate passwords or store them securely.
- A password passed on the command line can be visible in shell history and in process listings. Prefer testing a representative password rather than a real one you intend to keep using.
- Run the tool on a system with appropriate access controls.

### License information

This project is licensed under the GNU General Public License v3.0. See LICENSE in this repository.
