Running the program:

To the run the program simply open follow these instructions:
1. Open a terminal within the same directory as FileSystem.py
2. (If you have never ran this before) Compile and initalise the code using the command 'python3 FileSystem.py Filesystem -i' and follow the instructions
3. Once you have intialised the code with a user open a terminal and run 'python3 Filesystme.py Filesystem' and follow the instructions that follow in the terminal


Reduction Usage (Hash Functions)
I use hash functions in 3 sections of this assessment for different reasons. Line 56, 61, 81
- Line 56: I use MD5 here to hash the Password + Salt the user inputted before writing it to the Shadow file. This is so I can check the password in the main compiling as to not save the raw input of the user
- Line 61: The assessment asks us to call the MD5 function using the string "This is a test" to show the function works I presume
- Line 81: When running the script (not intialising it) we need to compare the users input with what exsists in the shadow file. We do this by hashing the users input, then looping through the shadow file to see if the hash exsists with the same username assoicated with it.
In summary, its to hash the users input (with a salt) and either add it to the shadow file or to check if it exsists in the shadow file.