# python3 encrypt.py
import random

# return substituion cipher with random assignments
def sub_cipher(char_list):

    letters = 'abcdefghijklmnopqrstuvwxyz'

    codings = {
        'a':'','b':'','c':'','d':'','e':'','f':'',
        'g':'','h':'','i':'','j':'','k':'','l':'',
        'm':'','n':'','o':'','p':'','q':'','r':'',
        's':'','t':'','u':'','v':'','w':'','x':'',
        'y':'','z':''
    }

    sub = ''
    cipher_text = ""

    # randomly assign letter substitutions
    for x in codings:
        sub = random.choice(letters)
        codings[x] = sub
        # remove sub from letters to avoid double mapping
        letters = letters.replace(sub,'')
    
    # output key
    print("\nSubstitution Key\n-----------------")
    print(codings)

    # create cipher text
    for y in char_list:
        if(y.islower()):
            cipher_text += codings[y]
            # Use same mappings for Upper case letters while maintaining case
        elif(y.isupper()):
            y = y.lower()
            cipher_text += codings[y].upper()
        else:
            cipher_text += y
    return cipher_text

# return caesar cipher text (original + offset)
# If letter + offset is beyond Z/z, rotates back to A/a
# symbols remain the same
def caesar_cipher(phrase_chars, offset):
    cipher_text = ""
    asc = 0
    for letter in phrase_chars:
        asc = ord(letter)
        # account for upper case letters
        if (asc >= 65 and asc <= 90):
            cipher_text += chr(((asc + offset - 65) % 26) + 65)
        # accout for lower case letters
        elif (asc >= 97 and asc <= 122):
            cipher_text += chr(((asc + offset - 97) % 26) + 97)
        else:
            cipher_text += letter
    return cipher_text

phrase = input('Enter phrase to encrypt with cipher: ')
enc_type = input('Enter number for Caesar cipher offset, or S for random substitution cipher: ')

phrase_chars = list(phrase)

if (enc_type == 'S' or enc_type == 's'):
    print("\nEncrypted phrase: " + sub_cipher(phrase_chars) + "\n")
elif (int(enc_type) >= 0 and int(enc_type) <= 26):
    print("\nEncrypted phrase: " + caesar_cipher(phrase_chars, int(enc_type)) + "\n")
else:
    print('invalid response')