def main():
    print(caesar_encrypt_fxn('PROFJUMPISCRAZYTOTHINKWECANDOTHIS',0))
    print(caesar_decrypt_fxn('SURIMXPSLVFUDCBWRWKLQNZHFDQGRWKLV',3))
alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def caesar_encrypt_fxn(string,key):
    encoded=''
    for i in string:
        newIndex=alphabet.index(i)+key
        if newIndex>=len(alphabet):
            newIndex=newIndex%len(alphabet)
        encoded+=alphabet[newIndex]
    return encoded

def caesar_decrypt_fxn(string,key):
    decoded=''
    for i in string:
        newIndex=alphabet.index(i)-key
        if newIndex<0:
            newIndex=newIndex%len(alphabet)
        decoded+=alphabet[newIndex]
    return decoded

if __name__=="__main__":
    main()