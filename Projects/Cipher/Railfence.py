def main():
    print(railfence_decrypt_fxn('PMAHCHRUPRZTIEATIOJICYONWNOSFSTKD',4))
    print(railfence_encrypt_fxn('PROFJUMPISCRAZYTOTHINKWECANDOTHIS',4))
def railfence_encrypt_fxn(string,key):
    if key==0:
        return string
    INTERVAL=(2*key-2)
    mid=INTERVAL//2
    delta=INTERVAL-mid
    encoded=''
    lister=[]
    while delta>=0:
        mid=INTERVAL//2
        while  mid-delta<=len(string):
            if mid-delta<=len(string)-1 and not mid-delta in lister:
                lister.append(mid-delta)
                encoded+=string[mid-delta]
            if mid+delta<=len(string)-1 and not mid+delta in lister:
                lister.append(mid+delta)
                encoded+=string[mid+delta]
            mid+=INTERVAL
        delta-=1
    return encoded

def railfence_decrypt_fxn(string,key):
    if key==0:
        return string
    interval=(2*key-2)
    mid=interval//2
    delta=interval-mid
    decodedList=[""]*len(string)
    decodedNumber=[]
    decoded=''
    while delta>=0:
        mid=interval//2
        while  mid-delta<=len(string):
            if mid-delta<=len(string)-1 and not mid-delta in decodedNumber:
                decodedNumber.append(mid-delta)
            if mid+delta<=len(string)-1 and not mid+delta in decodedNumber:
                decodedNumber.append(mid+delta)
            mid+=interval
        delta-=1
    for i in range(len(string)):
        decodedList[decodedNumber[i]]=string[i]
    for i in decodedList:
        decoded+=i
    return decoded

if __name__=='__main__':
    main()