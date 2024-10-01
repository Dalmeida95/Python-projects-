from cryptography.fernet import Fernet
import json
import random
import string

# Generate a key for encryption
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Load the previously generated key
def load_key():
    return open("secret.key", "rb").read()

# Encrypt a password
def encrypt_password(password):
    key = load_key()
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password

# Decrypt a password
def decrypt_password(encrypted_password):
    key = load_key()
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password).decode()
    return decrypted_password

# Function to save a password
def save_password(website, username, password):
    encrypted_password = encrypt_password(password)
    with open("passwords.json", "r+") as file:
        data = json.load(file)
        data[website] = {"username": username, "password": encrypted_password.decode()}
        file.seek(0)
        json.dump(data, file)

# Function to retrieve a password
def retrieve_password(website):
    with open("passwords.json", "r") as file:
        data = json.load(file)
        if website in data:
            encrypted_password = data[website]["password"].encode()
            username = data[website]["username"]
            decrypted_password = decrypt_password(encrypted_password)
            return username, decrypted_password
        else:
            return None
 
# Function to generate a random password
def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Main function to interact with the password manager
def main():
    while True:
        print("\nPassword Manager")
        print("1: Generate Password")
        print("2: Save Password")
        print("3: Retrieve Password")
        print("4: Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            length = int(input("Enter password length: "))
            password = generate_password(length)
            print(f"Generated Password: {password}")

        elif choice == "2":
            website = input("Enter website: ")
            username = input("Enter username: ")
            password = input("Enter password (or leave blank to generate): ")
            if not password:
                password = generate_password()
                print(f"Generated Password: {password}")
            save_password(website, username, password)
            print("Password saved successfully.")

        elif choice == "3":
            website = input("Enter website: ")
            result = retrieve_password(website)
            if result:
                username, password = result
                print(f"Username: {username}\nPassword: {password}")
            else:
                print("No password found for this website.")

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # Initialize the storage file (only run once to create the file)
    with open("passwords.json", "w") as file:
        json.dump({}, file)
    
    # Generate and save the encryption key (only run once)
    generate_key()
    
    # Run the main function
    main()
