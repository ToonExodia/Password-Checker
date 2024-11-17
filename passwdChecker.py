import hashlib
import os
import requests

# check password strength
def check_passwd_strength(password):
    score = 0
    feedback = []

#checks if password has appropriate length, numbers, uppaer case letters, and special charactesrs
    if len(password) >=8:
        score += 1
    else: feedback.append("Your password should be at least 8 characters long")

    if any(char.isdigit() for char in password):
        score += 1
    else: feedback.append("Add at least one number")

    if any(char.isupper() for char in password):
        score += 1
    else: feedback.append("Include at least 1 upper case letter")

    if any(char in "!@#$%^&*()-_=+[]{}|;:',.<>?/`~" for char in password):
        score += 1
    else: feedback.append("Add at least one special character")
    
    return score, feedback

# find a local worldlist
def find_wordlists(directory):
    wordlists = []
    for file in os.listdir(directory):
        if file.endswith(".txt"):
            wordlists.append(os.path.join(directory, file))
    return wordlists

# check password against the local wordlist
def check_passwd_wordlists (password, wordlist_path):
    try:
        with open(wordlist_path, 'r', encoding='latin-1') as file:
            for line in file:
                if password == line.strip():
                    return True
    except FileNotFoundError:
        print(f"Error: Wordlist file '{wordlist_path}' not found.")
    return False

# check password against Have I Been Pwned database
def check_passwd_HIBP(password):
    sha1_password = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix, suffix = sha1_password[:5], sha1_password[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            hashes = response.text.splitlines()
            for line in hashes:
                hash_suffix, count = line.split(":")
                if suffix == hash_suffix:
                    return True, int(count)
        else:
            print(f"Error: Could not connect to HIBP API. Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

    return False, 0


def main():
    password = input("\n Enter a password to check: ")

# check password strength
    score, feedback = check_passwd_strength(password)
    print(f"\nPassword Strength: {score}/4 ")
    if feedback:
        print("Suggestions for improvement:")
        for suggestion in feedback:
            print(f"- {suggestion}")
    else: print("Your password strength is good!")

# password against local wordlist
    print("\nChecking against local wordlists...")
    wordlists = find_wordlists(".")
    found_in_wordlist = False
    for wordlist in wordlists:
        print(f"Checking {os.path.basename(wordlist)}...")
        if check_passwd_wordlists(password, wordlist):
            print(f"WARNING: Your password is found in '{os.path.basename(wordlist)}'. Do not use it!")
            found_in_wordlist = True
            break
    if not found_in_wordlist: 
        print("Good news: Your password is not found in any local wordlists")

# password against HIBP database
    print("\nChecking against Have I Been Pwned database...")
    compromised, count = check_passwd_HIBP(password)
    if compromised:
        print(f"WARNING: Your password has been found in {count} data breaches! Do not use it. \n")
    else:
        print("Good news: Your password has not been found in known data breaches. \n")

        
if __name__ == "__main__":
    main()