import hashlib
import os

flag = 0
# paste the tested hashed code in the double quotation
real_hash = "0144e99a8cd56304aff370c875cbecb5"
try:
    file_path = os.path.join(os.path.dirname(__file__), 'guessed_pass.txt')
    guessed_pass = open(file_path ,"r")

    real_hashes_path = os.path.join(os.path.dirname(__file__), 'real_hashed.txt')
    real_hashes = open(real_hashes_path ,"r")

    for g_pass in guessed_pass:
        guessed_hash = hashlib.md5(g_pass.encode('utf8').strip()).hexdigest()
        for line in real_hashes:
            line = line.strip()
            print(guessed_hash == line)
            print(guessed_hash)
            print(line)
            print()
            if guessed_hash == line:
                print("Congratulations!")
                print("The real password of md5 hash is found" + line)
                print("It is "+ g_pass)
                # flag to 1 if password we found in the list
                flag = 1
                break
    # if no match from the file the flag still 0
    if flag == 0:
        # password is not in the list
        print("The plain password is not found in the guessed password file")

except e:
    print("Guessed password file is not found")
    print(e)

quit()