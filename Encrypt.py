"""
This program encrypts a text file using the vigenere algorithm
when you run the program, you need to pass three parameters, the first parameter is the name of the file, the second parameter is the key
the third parameter is optional and it is the name of the file you want to write the ciphertext to
if you don't pass a third parameter the program will only print "no file specified" and the ciphertext will appear on the CLI only
The algorithm will generate a ciphertext file without any special character or whitespaces
The algorithm will only consider encrypting english letters, uppercase letters will be converted to lowercase letters


example on how to run it from the CLI on windows: 
D:\Fall 2019>python encrypt.py "testfile.txt" "deceptive" "cipheredtext.txt"
where testfile.txt is the name of the plaintext file and deceptive is the keyword, and chipheredtext is the destination file

on Linux from terminal:
leen@pikachu:~/Documents$ python3 Encrypt.py "testfile.txt" "keyword" "ciphertext.txt"



please note that the length of the key should not exceed 10 characters and should not be less than one character
the key should not have any special characters or whitespaces

Leen Kilani 0154493
"""


# defining the main function in this program
def encrypt(plaintext, key):
    # creating a dictionary for indexed alphabet
    indexlist = list(range(0, 26))  # [0...25]
    asciilist = list(range(97, 123))  # ascii from 97 to 122

    alphabetlist = []
    for el in asciilist:
        alphabetlist.append(chr(el))  # convert ascii to character

    # now alphabetlist has ['a','b',...'z']

    alphabet = dict(zip(alphabetlist, indexlist))  # {'a':0, 'b':1, ... 'z':25}
    alphabet2 = dict(zip(indexlist, alphabetlist))  # {0:'a'... 25:'z'}

    # removing special characters and whitespaces from plaintext
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in plaintext:
        if (char not in letters):
            plaintext = plaintext.replace(char, "")
    plaintext = plaintext.lower()  # making sure everything is in lowercase

    import math
    # duplicating the key so that it has greater than or equal number of characters as plaintext
    x = math.ceil((len(plaintext) / len(key)))
    key = key * x

    ciphertext = ''
    # this is the basic vigenere algorithm
    for i, letter in enumerate(plaintext):
        # here, i is the index of each letter in plaintext, using enumerate

        # newchar has the corresponding number of the encrypted letter
        newchar = (alphabet[letter] + alphabet[key[i]]) % 26
        # the ecnrypted letter is appended to ciphertext
        ciphertext += alphabet2[newchar]

    return ciphertext


if __name__ == '__main__':
    import sys

    # reading the first argument, plaintext file path/name
    try:
        with open(sys.argv[1], 'r') as textfile:
            plaintext = textfile.read()
    except IndexError:
        print("please rerun the script with the correct arguments")
        print(
            "python Encrypt.py [input file name] [key, no whitespaces or special characters] [output file name, optional]")
        sys.exit(0)
    else:
        pass

    # reading the second argument, the keyword
    key = sys.argv[2]
    if (len(key) < 1 or len(key) > 10):
        print("key length exceeds limits")
        print("key length should be between 1 and 10 characters")
        print("please rerun the script with the correct arguments")
        sys.exit(0)

    # calling the main function
    ciphertext = encrypt(plaintext, key)

    print(ciphertext)

    # writing ciphertext to the specified filepath/name
    try:
        f = open(sys.argv[3], 'w')
    except IndexError:
        print("\nno output file specified")

    else:
        f.write(ciphertext)
        f.close()
