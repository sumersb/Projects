def main():
    streamingfxn()

def streamingfxn():
    continuater='y'
    if continuater=='y':
        prompt()
        continuater=input("If you would like to continue for another streaming service press 'y': ").lower()
    
def prompt():
    countPeople,countWatcher,over25Local,over25Foreign,under25Local,under25Foreign=0,0,0,0,0,0

    while True:
        countPeople+=1
        age=age_fxn()

        residency=residence_fxn()

        regular=regular_fxn()

        if regular=='y':
            countWatcher+=1
            if age<25:
                if residency=='l':
                    under25Local+=1
                else: under25Foreign+=1
            else:
                if residency=='l':
                    over25Local+=1
                else:over25Foreign+=1

        cont=continue_fxn()
        if cont!='y':
            break
    summary_fxn(countPeople,countWatcher,over25Local,over25Foreign,under25Local,under25Foreign)

def summary_fxn(countPeople,countWatcher,over25Local,over25Foreign,under25Local,under25Foreign):    
    under25LocalPercent=round(under25Local/countWatcher*100)
    over25LocalPercent=round(over25Local/countWatcher*100)
    localTotalPercent=under25LocalPercent+over25LocalPercent
    under25ForeignPercent=round(under25Foreign/countWatcher*100)
    over25ForeignPercent=round(over25Foreign/countWatcher*100)
    foreignTotalPercent=under25ForeignPercent+over25ForeignPercent
    under25Percent=under25ForeignPercent+under25LocalPercent
    over25Percent=over25LocalPercent+over25ForeignPercent

    print('The total number of people called = ',countPeople)
    print("The total number of people who use the streaming service regularly = ",countWatcher)
    print("The percentage of those who use the streaming service regularly = ",round(countWatcher//countPeople))
    print('')
    print('-----------------------------------------------------------------------')
    print('Residency          %under 25           %25 or Over              %total')
    print('-----------------------------------------------------------------------')
    print('Local                ',under25LocalPercent,'                  ',over25LocalPercent,'                  ',localTotalPercent)
    print('')
    print('Foreigner            ',under25ForeignPercent,'                  ',over25ForeignPercent,'                  ',foreignTotalPercent)
    print('-------------------------------------------------------------------------')

    print('Total                ',under25Percent,'                  ',over25Percent,'                  ',100)
    print('-------------------------------------------------------------------------')

        


def age_fxn():
    print('Enter your age: ')
    oldness=int(input(''))
    if oldness>120 or oldness<1:
        print('Invalid age input')
        return age_fxn()
    else: return oldness

def residence_fxn():
    print("Please enter this person's residency status (L/F')")
    location=input('')
    if location.lower() !='l' and location.lower()!='f':
        print('Invalid input')
        return residence_fxn()
    return location.lower()
    
def regular_fxn():
    print('Please enter whether this person use streaming services regularly (Y/N) : ')
    isWatcher=input('')
    if isWatcher.lower()!='y' and isWatcher.lower()!='n':
        print('Invalid input')
        return regular_fxn()
    return isWatcher.lower()

def continue_fxn():
    print("Do you want to enter another person's details (Y/N)?")
    keepGoing=input('')
    if keepGoing.lower()!='y' and keepGoing.lower()!='n':
        print('Invalid input')
        return continue_fxn()
    else:return keepGoing.lower()


if __name__=='__main__':
    main()