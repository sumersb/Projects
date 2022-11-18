import re
from Railfence import *
from Caesar import *
def main():
    cipher()

def cipher():
    code='SUPER SECRET AGENT CODING TIME :)))))'
    while code!='y':
        print('Select from an option below')
        print('1 - Encrypt')
        print('2 - Decrypt')
        print('3 - Quit')
        code=input('Enter your choice: ')
        match code:
            case '1':
                string=input('Enter a string to be encoded (all punctuation, number and spaces will be removed): ')
                string=validate_string_fxn(string)
                key=input('Enter a positive integer to be your key: ')
                key=validate_key_fxn(key)
                string=caesar_encrypt_fxn(string,key)
                string=railfence_encrypt_fxn(string,key)
                print("Encoded string: ",string)

            case '2':
                string=input('Enter a string to be decoded (all punctuation, number and spaces will be removed): ')
                string=validate_string_fxn(string)
                key=input('Enter a positive integer to be your key: ')
                key=validate_key_fxn(key)
                string=railfence_decrypt_fxn(string,key)
                string=caesar_decrypt_fxn(string,key)
                print("Decoded string: ",string)
            case '3':
                quit



def validate_string_fxn(string):
    valid_str=''
    for letter in string:
        if letter.isalpha():
            valid_str+=letter.upper()
    return valid_str

def validate_key_fxn(key):
    while not re.match("^\d+$",key):
        print('Invalid key')
        key=input('Enter a positive integer to be your key: ')
    return int(key)
         
if __name__=='__main__':
    main()