import getpass
import string
import random
import hashlib

def main():
    print("Hello World")
    Menu = True

    while (Menu):
        user_input = input()
        print(user_input)
        Menu = False
        match user_input:
            case "Filesystem -i":
                password_check = True
                print("File")
                username = input("Username: ")
                while password_check:
                    password = getpass.getpass('Password: ')
                    confirm_password = getpass.getpass('Confirm Password:')
                    if (password == confirm_password):
                        password_check = False
                    else:
                        print("Your passwords did not match please try again")

                    user_clearance = input("User clearance (0 or 1 or 2 or 3): ")

                    user_with_salt = username + ''.join(random.choice(string.digits) for _ in range(8))

                    salt_file = open('salt.txt', 'a')
                    salt_file.write(user_with_salt)
                    salt_file.close()

                    
                    hash = hashlib.md5(user_with_salt.encode())
                    with open("shadow.txt", "w") as file:
                        file.write(hash.hexdigest() + ":" + user_clearance)

            case "Filesystem":
                print("In-Progress")

if __name__ == "__main__":
    main()