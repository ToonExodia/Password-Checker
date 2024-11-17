# **Enhanced Password Strength and Compromise Checker**

A Python program to evaluate password strength and check if passwords are compromised using both local wordlists and the Have I Been Pwned (HIBP) API.  

This project demonstrates Python concepts like file handling, API requests, and dynamic wordlist detection.

---

## **Features**
- Checks password strength based on:
  - Length
  - Presence of numbers, uppercase letters, and special characters.
- Detects compromised passwords in:
  - Local wordlists (e.g., `rockyou.txt`).
  - Online databases using the Have I Been Pwned API.
- Automatically identifies all `.txt` wordlists in the same directory.
- Provides actionable feedback on improving password strength.

---

## **Installation**
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/password-checker.git
   cd password-checker
2. Install dependencies:
- Python 3.7 or higher is required.
- Install the `requests` library for API calls:
  ```bash
  pip install requests
3. (Optional) Download the RockYou wordlists:
- Place the `rockyou.txt` file or any other `.txt` wordlist in the same directory as the script

---

## **How to Use**
### **Run the Program**
1. Open a terminal and navigate to the project directory.
2. Run the program:
   ```bash
   python passwdChecker.py
### **Input**
- The program prompts you to enter a password for analysis
### **Output**
- The password's strength score (out of 4) and suggestions for improvement
- A warning if the password is found in:
  - A Local wordlist
  - Known data breaches via the Have I been Pwned API

---

## **Examples**
### **Example 1: Weak Password (with no local wordlist)**
#### **Input:**
```bash
Enter a password to check: 12345
```
#### **Output:**
```bash
Password Strength: 1/4 
Suggestions for improvement:
- Your password should be at least 8 characters long
- Include at least 1 upper case letter
- Add at least one special character

Checking against local wordlists...
Good news: Your password is not found in any local wordlists

Checking against Have I Been Pwned database...
WARNING: Your password has been found in 3510539 data breaches! Do not use it.
```
### **Example 2: Weak Password (with local wordlist)**
#### **Input:**
```bash
Enter a password to check: 12345
```
#### **Output:**
```bash
Password Strength: 1/4 
Suggestions for improvement:
- Your password should be at least 8 characters long
- Include at least 1 upper case letter
- Add at least one special character

Checking against local wordlists...
Checking rockyou.txt...
WARNING: Your password is found in 'rockyou.txt'. Do not use it!

Checking against Have I Been Pwned database...
WARNING: Your password has been found in 3510539 data breaches! Do not use it.
```


### **Example 3: Strong Password**
#### **Input:**
```bash
Enter a password to check: !W86r563ofNCTqXf
```
#### **Output:**
```bash
Password Strength: 4/4 
Your password strength is good!

Checking against local wordlists...
Good news: Your password is not found in any local wordlists

Checking against Have I Been Pwned database...
Good news: Your password has not been found in known data breaches. 
```
