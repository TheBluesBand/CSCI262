import getpass
import string
import random
import hashlib
import sys

def main():
    print("Hello World")
    Menu = True

    while (Menu):
        user_input = input()
        print(user_input)
        Menu = False

        #for arg in sys.argv:
        #    print(arg)


        match user_input:
            case "Filesystem -i":
                password_check = True
                print("File")
                username = input("Username: ")
                username = username.strip()
                while password_check:
                    password = getpass.getpass('Password: ')
                    confirm_password = getpass.getpass('Confirm Password:')
                    if (password == confirm_password):
                        password_check = False
                    else:
                        print("Your passwords did not match please try again")

                    user_clearance = input("User clearance (0 or 1 or 2 or 3): ")

                    
                    salt = ''.join(random.choice(string.digits) for _ in range(8))
                    hash_input = password + salt
                    file_input = username + ":" + salt

                    salt_file = open('salt.txt', 'a')
                    salt_file.write(file_input + '\n')
                    salt_file.close()

                    
                    hash = hashlib.md5(hash_input.encode())
                    with open("shadow.txt", "a") as file:
                        file.write(username + ":" + hash.hexdigest() + ":" + user_clearance + '\n')

            case "Filesystem":
                username = input("Username: ")
                #check for secure password
                password = getpass.getpass('Password: ')
                valid_details = False

                with open("salt.txt", "r") as file:
                    for line in file:
                        if username in line:
                            print(username + " found in salt.txt")
                            salt = line.find(username)
                            if salt != -1:
                                salt = line[salt + len(username) + 1:].strip()
                            else:
                                salt = ""

                            print("Salt retrieved: " + salt)
                            print("Hashing...")
                            password = password + salt
                            hash = hashlib.md5(password.encode())
                            print("Hash value: " + hash.hexdigest())
                            with open("shadow.txt", 'r') as shadow:
                                lines = shadow.readlines()
                                for new_line in lines:
                                    if hash.hexdigest() in new_line:
                                        valid_details = True
                                        print("Authentication for user " + username + " complete.")
                                        print("The clearance for " + username + " is " + new_line.strip()[-1] + ".\n")
                        else:
                            print("Username not found")

                while (valid_details):
                    menu_selection = input("Options: (C)reate, (A)ppend, (R)ead, (W)rite, (L)ist, (S)ave or (E)xit. ")
                    match menu_selection:
                        case "C":
                            print("C")
                            user_input = input("Filename: ")
                            file = open("FileSystemRecords.txt", "r")
                            for line in file:
                                if user_input in file:
                                    print()
                                    
                        case "A":
                            print("A")
                        case "R":
                            print("R")
                        case "W":
                            print("W")
                        case "L":
                            print("LIST")
                            file = open("Files.store", "r")
                            for line in file:
                                print(line)
                                    
                        case "S":
                            print("S")
                        case "E":
                            end = input("Shut down the FileSystem (Y)es or (N)o ")
                            if end == 'Y':
                                valid_details = False



if __name__ == "__main__":
    main()