import math
import sys


# Input: strng is a string of 100 or less of upper case, lower case,
#        and digits
# Output: function returns an encrypted string

def encrypt(strng):
    '''Inputs a string of 100 characters or less of upper case, lower case,
     or digits, and 'encrypts' them by entering them in a 2D list, then rotating
     the list.'''

    # Initializations
    L = len(strng)
    M = math.ceil(math.sqrt(L))
    message = ''

    # Creates a list called 'encryptlist' for each character of the string to be in
    encryptlist = []
    for i in strng:
        encryptlist.append(i)

    # Creates a 2D list called 'encryption_spiral', currently full of asterisks
    encryption_spiral = [["*" for i in range(M)] for j in range(M)]

    # For each column, for each row, add each character from 'encryptlist' to the 'encryption_spiral' in row-major order
    i = 0
    for column in range(M):
        for row in range(M):
            if i < len(encryptlist):
                encryption_spiral[column][row] = encryptlist[i]
                i += 1

    # Creates a list called 'rotated_encryption_spiral', as a template to rotate the 'encryption_spiral'
    rotated_encryption_spiral = [["*" for i in range(M)] for j in range(M)]

    # Rotates 'encryption_spiral' by adding its respective values into their respective places in 'rotated_encryption_spiral'
    for column in range(M):
        for row in range(M):
            if len(encryption_spiral) > 0:
                rotated_encryption_spiral[column][row] = encryption_spiral[(M - 1) - row][column]

    # Creates the return value, 'message', by running across each column and each row, and appending each character to the end of a string.
    for column in range(M):
        for row in range(M):
            if rotated_encryption_spiral[column][row] != "*":
                message += rotated_encryption_spiral[column][row]

    # Returning 'message'
    return message


# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string

def decrypt(strng):
    '''Inputs a string of 100 characters or less of upper case, lower case,
     or digits, and 'decrypts' them. Firstly, it formats them as if they had been
     outputted from the 'encrypt' function. Then, it rotates the output list.'''

    # Initializations
    L = len(strng)
    M = math.ceil(math.sqrt(L))

    # Creates a list called 'decryptLst' for each character of the string to be in
    decryptLst = []
    for i in strng:
        decryptLst.append(i)

    # Creates a 2D list called 'decryption_spiral', currently full of asterisks
    decryption_spiral = [["*" for i in range(M)] for j in range(M)]

    # For each column, for each row, add each character from 'decryptLst' to the 'decryption_spiral' in row-major order
    i = 0
    for column in range(M):
        for row in range(M):
            if i < len(decryptLst):
                decryption_spiral[column][row] = decryptLst[i]
                i += 1

    # A flurry of initializations, designed to create 4 empty spirals, in preparation for the subsequent rotating and formatting
    rotated_decryption_spiral = [["*" for i in range(M)] for j in range(M)]
    prepared_spiral = [["*" for i in range(M)] for j in range(M)]
    secondary_spiral = [["*" for i in range(M)] for j in range(M)]
    final_spiral = [["*" for i in range(M)] for j in range(M)]

    # Fill the 'rotated_decryption_spiral' array with '['s in every position where there was a character. This marks the position of the character
    # NOTE: '[' cannot be in the original string, and is therefore a safe value to use as a placeholder
    i = 0
    for column in range(M):
        for row in range(M):
            if i < len(decryptLst):
                rotated_decryption_spiral[column][row] = "["
                i += 1

    # Fill the 'prepared_spiral' array with a rotated version of the 'rotated_decryption_spiral'. The positions of
    # the new rotation should now be marked with '['s
    for column in range(M):
        for row in range(M):
            if len(rotated_decryption_spiral) > 0:
                prepared_spiral[column][row] = rotated_decryption_spiral[(M - 1) - row][column]

    # Fill the 'secondary_spiral' array by scanning each element of the 'prepared_spiral', adding asterisks where
    # relevant. If it scans a '[', it adds the next relevant character of the string instead. This maintains
    # row-major order
    i = 0
    for column in range(M):
        for row in range(M):
            if len(secondary_spiral) > 0:
                if prepared_spiral[column][row] == "*":
                    secondary_spiral[column][row] = "*"
                elif prepared_spiral[column][row] == "[":
                    secondary_spiral[column][row] = decryptLst[i]
                    i += 1

    # Fill the 'final_spiral' array with a rotated version of the 'secondary_spiral', rotating back to the correct orientation.
    for column in range(M):
        for row in range(M):
            if len(final_spiral) > 0:
                final_spiral[column][row] = secondary_spiral[row][(M - 1) - column]

    # Creates the return value, 'message', by running across each column and each row, and appending each character to the end of a string.
    message = ''
    for row in range(M):
        for column in range(M):
            if final_spiral[row][column] != "*":
                message += final_spiral[row][column]

    # Returning 'message'
    return message


def main():
    # read the strings P and Q from standard input
    in_file = sys.stdin.read()
    fileLst = in_file.split("\n")
    P, Q = fileLst[0], fileLst[1]

    # encrypt the string P
    a = encrypt(P)
    # decrypt the string Q
    b = decrypt(Q)
    # print the encrypted string of P
    # and the decrypted string of Q

    print(a)
    print(b)


if __name__ == "__main__":
    main()
