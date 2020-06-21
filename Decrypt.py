"""
This program decrypts a ciphered text  without the key using the vigenere algorithm 
When you run the program you need to specify at least one input, maximum two inputs
The first input is the file name of the ciphered text that you want to decrypt
The second input is the file name of the output file that you want to write the output to
The program first finds the key size and prints it then it will print the plain/decrypted text
then it will print a list of possible english words

how to run from terminal on Linux:
leen@pikachu:~/Documents$ python3 Decrypt.py "ciphertext.txt" "plaintextout.txt"

Leen Kilani 0154493

"""


def freq(letter, text):
    # this function is used to calcualte the frequency of a given letter in a given text
    count = 0
    for char in text:
        if (letter == char):
            count += 1
    return count / len(text)


def findKeySize(ciphertext):
    # this functoin is used to find the key size of given ciphered text

    keySizes = {}  # holds possible key sizes as keys and the corresponding frequency sum as values

    for keysize in range(1, 11):  # maximum key size is 10, minimum is 1
        newText = ciphertext[::keysize]  # slice the text based on the current keysize

        # dictionary of default freq of each alphabet set to zeros {'a':0,...'z':0}
        frequencies = dict(zip(alphabetlist, list1))

        sum = 0  # everytime the sum of frequencies of each keysize will reset to zero
        for letter in newText:
            frequencies[letter] = freq(letter, newText)  # find the freq of each letter in the sliced text
        for val in frequencies.values():  # find the sum of the squared frequencies
            sum += (val * val)
        if (round(sum, 3) >= 0.055 and round(sum, 3) <= 0.075):  # find possible keysizes
            keySizes[keysize] = sum

    difflist = []  # holds the difference of each frequency with 0.065
    # to evaluate wich keysize has frequency closer to 0.065
    for k, v in keySizes.items():
        difflist.append(abs(0.065 - v))
        if (v == 0.065):
            return k
        elif (round(v, 3) == 0.065 or (round(v, 4) >= 0.064 and round(v, 4) <= 0.066)):
            return k
        elif (round(v, 4) >= 0.063 and round(v, 4) <= 0.067):
            return k
        elif (round(v, 4) >= 0.062 and round(v, 4) <= 0.068):
            return k
        elif (round(v, 4) >= 0.061 and round(v, 4) <= 0.069):
            return k
        elif (round(v, 4) >= 0.06 and round(v, 4) <= 0.07):
            return k
        elif (round(v, 4) >= 0.059 and round(v, 4) <= 0.071):
            return k
        elif (round(v, 4) >= 0.058 and round(v, 4) <= 0.072):
            return k
        elif (round(v, 4) >= 0.057 and round(v, 4) <= 0.073):
            return k
    for k, v in keySizes.items():
        if (min(difflist) == abs(0.065 - v)):
            return k


def Decrypt(keysize, ciphertext):
    # now we know the key size, time to decrypt
    workingText = [x for x in ciphertext]  # cast the ciphertext into a list of characters
    mapping = {}  # will hold the corresponding character for every char in the C text after freq analysis
    frequencies = dict(zip(alphabetlist, list1))

    for i in range(0, keysize):
        # slice the ciphertext by the length of the keysize
        # the range of the starting point of the slice is from zero to keysize-1
        # to make sure we got all the characters
        # this loop will treat every new sliced text as one text
        # and then move on to the next portion depending on the keysize
        newText = ciphertext[i::keysize]
        for char in newText:
            frequencies[char] = freq(char, newText)
            # calculate the freq of each character and save it

        mapping = freqAnalysis(frequencies)
        # e.g {'e':'h', 't':'v'...,'z':'l'}

        for j in range(i, len(workingText), keysize):
            # this way the range index of j corresponds to the sliced text only
            # workingText is a list for easier manipulation and indexing
            for k, v in mapping.items():
                # replace the characters by the decrypted characters
                if (ciphertext[j] == k):
                    workingText[j] = v

    decrypted = ''.join(workingText)  # cast the list into a string
    return decrypted


def freqAnalysis(dictionary):
    plainDict = {}  # dict of mapping of each charcter to the decrypted character
    freqList = []  # a list of the frequencies of each character in the Ctext

    # make a list of each character starting from highest occurence to the lowest
    # based on freq analysis
    alphabeticOrder = [x for x in "etaoinsrhdlucmfywgpbvkxqjz"]

    for v in dictionary.values():
        freqList.append(v)

    # sort the list from highest freq to lowes freq
    # to map it with the alphabeticOrder list    
    freqList.sort(reverse=True)

    newList = []  # freq arranged alphabet list
    for i in range(0, 26):
        for k, v in dictionary.items():
            if (freqList[i] == v):
                newList.append(k)

    plainDict = dict(zip(newList, alphabeticOrder))

    return plainDict


def possibleWords(plainText):
    import enchant
    d = enchant.Dict('en')
    words3 = ['\n3 letter words: \n']
    words4 = ['\n\n4 letter words: \n']
    words5 = ['\n\n5 letter words: \n']
    words6 = ['\n\n6 letter words: \n']
    words7 = ['\n\n7 letter words: \n']

    # check for different lengths of words
    for i in range(0, len(plainText)):
        wrd = plainText[i:i + 3]
        if (d.check(wrd) and len(wrd) == 3):
            words3.append(wrd)

        wrd = plainText[i:i + 4]
        if (d.check(wrd) and len(wrd) == 4):
            words4.append(wrd)

        wrd = plainText[i:i + 5]
        if (d.check(wrd) and len(wrd) == 5):
            words5.append(wrd)

        wrd = plainText[i:i + 6]
        if (d.check(wrd) and len(wrd) == 6):
            words6.append(wrd)

        wrd = plainText[i:i + 7]
        if (d.check(wrd) and len(wrd) == 7):
            words7.append(wrd)

    words = words3 + words4 + words5 + words6 + words7

    return words


if __name__ == '__main__':
    import sys

    try:
        with open(sys.argv[1], 'r') as textfile:
            ciphertext = textfile.read()
    except IndexError:
        print("please rerun the script with the correct arguments")
        print("python Decrypt.py [input file name] [output file name, optional]")
        sys.exit(0)
    else:
        pass

    list1 = [0] * 26
    asciilist = list(range(97, 123))
    alphabetlist = []
    for el in asciilist:
        alphabetlist.append(chr(el))

    k_size = findKeySize(ciphertext)
    print("Key size: ", k_size)
    plainText = Decrypt(k_size, ciphertext)
    words = possibleWords(plainText)
    print("\n************************************\nPrinting decrypted text:\n", plainText)
    print("\n************************************\nPrinting possible words:\n")
    print(*words, sep=', ')
    try:
        f = open(sys.argv[2], 'w')
    except IndexError:
        print("\nno output file specified")
    else:
        f.write(plainText)
        f.close()
