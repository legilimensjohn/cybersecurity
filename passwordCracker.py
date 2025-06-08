import hashlib

def crack_password(hash_to_crack, wordlist):
    with open(wordlist, 'r') as f:
        for line in f:
            password = line.strip()
            hashed = hashlib.sha256(password.encode()).hexdigest()
            if hashed == hash_to_crack:
                return password
    return None

if __name__ == "__main__":
    # Example usage
    hash_input = input("Enter SHA-256 hash to crack: ").strip()
    wordlist_path = input("Enter path to wordlist: ").strip()
    result = crack_password(hash_input, wordlist_path)
    if result:
        print(f"Password found: {result}")
    else:
        print("Password not found in wordlist.")
