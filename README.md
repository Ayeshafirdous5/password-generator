# 🔐 Password Generator

A simple and customizable Python CLI tool to generate strong and secure passwords.

---

## 🚀 Features

* Generate passwords with custom length
* Option to include numbers and symbols
* Avoid confusing characters (like `0`, `O`, `l`, `1`)
* Password strength checker (Weak / Medium / Strong)
* Copy password to clipboard

---

## 🧠 Password Strength Logic

The strength of the generated password is determined based on the following criteria:

### 🔴 Weak

* Password length is less than 8 characters
* OR contains only letters (no numbers or symbols)

### 🟡 Medium

* Password length is at least 8 characters
* Contains some variation but does not meet all strong criteria

### 🟢 Strong

* Password length is 12 or more characters
* Includes:

  * Uppercase letters
  * Numbers
  * Symbols

---

## 🛠️ Requirements

* Python 3.x
* `pyperclip` library

Install dependency:

```bash
pip install pyperclip
```

---

## ▶️ How to Run

```bash
python main.py
```

---

## 📸 Example Output

```
Enter password length: 12
Include numbers? y
Include symbols? y
Avoid similar characters? y

Generated Password: Xy7@KpLm#9Qa
Strength: Strong
```

---

## 📌 Future Improvements

* GUI version using Tkinter
* Advanced password strength meter
* Save passwords securely

---

## 💻 Author

Ayesha Firdous
