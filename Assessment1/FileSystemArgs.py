import getpass
import string
import random
import hashlib
import sys
import re
import os

def main():
    print("Hello World")
    Menu = True

    while (Menu):
        Menu = False

        for arg in sys.argv:
            print(arg)

        print(sys.argv)
        if (sys.argv[1] == "Filesystem" and len(sys.argv) > 2 and sys.argv[2] == "-i"):
            password_check = True
            print("File")
            username = input("Username: ")
            username = username.strip()
            while password_check:
                password = getpass.getpass('Password: ')
                confirm_password = getpass.getpass('Confirm Password:')
                if (password == confirm_password):
                    password_check = False

                    #Check if the string contains at least 8 characters
                    if len(password) < 8:
                        password_check = True
                    
                    # Check if the string contains at least one digit
                    if not re.search(r'\d', password):
                        password_check = True
                    
                    # Check if the string contains at least one special character
                    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
                        password_check = True
                        print("Password did not contain at least 8 characters, a numeric digit and a special character")
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

        if (sys.argv[1] == "Filesystem" and len(sys.argv) == 2):
            print('MD5("This is a test") = ' + hashlib.md5("This is a test".encode()).hexdigest() + '\n')
            username = input("Username: ")
            password = getpass.getpass('Password: ')

            valid_details = False
            user_clearance = 0

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
                                    user_clearance = new_line.strip()[-1]
                                    print("Authentication for user " + username + " complete.")
                                    print("The clearance for " + username + " is " + new_line.strip()[-1] + ".\n")

            if(valid_details == False):
                print("Username not found")

            temp_entries = []
            if not os.path.exists("Files.store"):
                with open("Files.store", 'w'):
                    pass
        
            while (valid_details):
                menu_selection = input("Options: (C)reate, (A)ppend, (R)ead, (W)rite, (L)ist, (S)ave or (E)xit. ")
                if menu_selection == "C":
                    user_input = input("Filename: ")
                    file = open("Files.store", "r")
                    found = False

                    for line in file:
                        if user_input in file:
                            found = True

                    if (found):
                        print("That file name exists please try again with a new name")
                    else:
                        temp_entries.append(user_input + ":" + username + ":" + user_clearance)
                                
                if menu_selection == "A":
                    file_name = input("Filename: ")
                    file = open("Files.store", "r")
                    found = False
                    file_temp = ""

                    #Check files in File.store
                    for line in file:
                        if file_name in str(line):
                            found = True
                            file_temp = line

                    #Check for files in unsaved files
                    for line in temp_entries:
                        if file_name in line:
                            found = True
                            file_temp = file_name.strip()

                    if len(file_temp) > 0:
                        if (found and (int(file_temp[-2]) <= int(user_clearance))):
                            print("Appened to a file!")
                        else:
                            print("You do not have access to that file!")

                if menu_selection == "R":
                    file_name = input("Filename: ")
                    file = open("Files.store", "r")
                    found = False
                    file_temp = ""

                    #Check files in File.store
                    for line in file:
                        if file_name in str(line):
                            found = True
                            file_temp = line

                    #Check for files in unsaved files
                    for line in temp_entries:
                        if file_name in line:
                            found = True
                            file_temp = file_name.strip()

                    if len(file_temp) > 0:
                        if (found and (int(file_temp[-2]) <= int(user_clearance))):
                            print("You read the file!")
                        else:
                            print("You do not have access to that file!")

                if menu_selection == "W":
                    file_name = input("Filename: ")
                    file = open("Files.store", "r")
                    found = False
                    file_temp = ""

                    #Check files in File.store
                    for line in file:
                        if file_name in str(line):
                            found = True
                            file_temp = line

                    #Check for files in unsaved files
                    for line in temp_entries:
                        if file_name in line:
                            found = True
                            file_temp = file_name.strip()

                    if len(file_temp) > 0:
                        if (found and (int(file_temp[-2]) <= int(user_clearance))):
                            print("You wrote to the file!")
                        else:
                            print("You do not have access to that file!")

                if menu_selection == "L":
                    file = open("Files.store", "r")
                    for line in file:
                        print(line)
                    for line in temp_entries:
                        print(line)
                            
                if menu_selection == "S":
                    with open("Files.store", 'a') as file:
                        for item in temp_entries:
                            file.write(str(item) + '\n')

                    temp_entries = []

                if menu_selection == "E":
                    end = input("Shut down the FileSystem (Y)es or (N)o ")
                    if end == 'Y':
                        valid_details = False



if __name__ == "__main__":
    
    main()