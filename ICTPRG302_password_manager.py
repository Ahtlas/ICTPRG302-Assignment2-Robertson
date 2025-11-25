#Function to display menu
def show_menu():
    print("\nPassword Manager:")
    print("1. Add Credentials")
    print("2. View Credentials")
    print("3. Exit")
    choice = input("Choose an option: ").strip() #Strip whitespace
    return choice

import os

#File to store credentials
FILENAME = "credentials.txt"

#ROT3 Encryption
def rot3_encrypt(text):
    encrypted = []
    for char in text:
        if char.isalpha(): #Only encrpt alphabetic characters
            shift = 3
            base = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted.append(encrypted_char)
        else: #Non-alphabetic characters remain unchanged
            encrypted.append(char)
    return ''.join(encrypted)

#ROT3 Decryption
def rot3_decrypt(text):
    decrypted = []
    for char in text:
        if char.isalpha():
            shift = 3
            base = ord('a') if char.islower() else ord('A')
            decrypted_char = chr((ord(char) - base - shift) % 26 + base)
            decrypted.append(decrypted_char)
        else:
            decrypted.append(char)
    return ''.join(decrypted)

#Create the credentials file if it doesn't exist
def create_file_if_missing():
    try:
        if not os.path.exists(FILENAME):
            with open(FILENAME, 'w') as f:
                pass
    except PermissionError:
        print(f"[ERROR] Permission denied: Cannot create {FILENAME}. Please check your folder permissions.")
    except Exception as e:
        print(f"[ERROR] Could not create {FILENAME}: {e}")

#Add new credentials/inputs
def add_credentials():
    username = input("Enter username: ")
    password = input("Enter password: ")
    resource = input("Enter URL or resource: ")

    #Encrypt credentials/inputs
    enc_username = rot3_encrypt(username)
    enc_password = rot3_encrypt(password)
    enc_resource = rot3_encrypt(resource)

    #Append encrypted credentials to file
    with open(FILENAME, 'a') as f:
        f.write(f"{enc_username},{enc_password},{enc_resource}\n")

        print("Credentials added successfully.")

#View stored credentials
def view_credentials():
    print("Stored Credentials:")
    print("{:<20} {:<20} {:<20}".format("Username", "Password", "Resource"))
    print("-" * 60)

    credentails_list = [] #Data structure?

    with open(FILENAME, 'r') as f:
        for line in f:
            line = line.strip()

            if not line:
                continue  # Skip empty lines
            
            enc_username, enc_password, enc_resource = line.strip().split(',')
            #Decrypt credentials
            username = rot3_decrypt(enc_username)
            password = rot3_decrypt(enc_password)
            resource = rot3_decrypt(enc_resource)
            #Display spaced out 
            print("{:<20} {:<20} {:<20}".format(username, password, resource))

            credentails_list.append((username, password, resource)) #Tuple

    for item in credentails_list:
        print("{:<20} {:<20} {:<20}".format(item[0], item[1], item[2]))

#Main program loop
def main():
    create_file_if_missing() #Ensure file exists
    while True:
        choice = show_menu() #Display menu and get user choice
        if choice == '1':
            add_credentials()
        elif choice == '2':
            view_credentials()
        elif choice == '3':
            print("Exiting Program.")
            break
        else:
            print("Invalid choice. Please try again.")

#Run the program    
if __name__ == "__main__":
    main()