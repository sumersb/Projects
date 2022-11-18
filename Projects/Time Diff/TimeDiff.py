import re
def main():
    userTime()

def userTime():
    continuer='y'
    while continuer=='y':
        start=input('Enter a start time in the format hh:mm am/pm: ')
        while not re.match("^[1-9]:[0-5][0-9]\s[ap]m$|^[1][0-2]:[0-5][0-9]\s[ap][m]",start):
            print('Invalid Input')
            start=input('Enter a start time in the format hh:mm am/pm: ')
        end=input('Enter a end time in the format hh:mm am/pm: ')
        while not re.match("^[1-9]:[0-5][0-9]\s[ap]m$|^[1][0-2]:[0-5][0-9]\s[ap][m]",end):
            print('Invalid Input')
            end=input('Enter a end time in the format hh:mm am/pm: ')
        minutes=time_diff(start,end)
        print('A difference of ',minutes,' minutes.')
        continuer=input("Press 'y' to go again: ")

def time_diff(startTime,endTime):
    totalStart=0
    totalEnd=0
    minInHour=60
    startTimeList=startTime.split()
    startDayTime=startTimeList[1]
    startTimeList=startTimeList[0].split(':')
    startHour=int(startTimeList[0])
    startMinute=int(startTimeList[1])
    if startDayTime=='pm':
        totalStart+=720
    if startHour==12:
        totalStart+=startMinute
    else:
        totalStart+=startHour*minInHour+startMinute

    endTimeList=endTime.split()
    endDayTime=endTimeList[1]
    endTimeList=endTimeList[0].split(':')
    endHour=int(endTimeList[0])
    endMinute=int(endTimeList[1])
    if endDayTime=='pm':
        totalEnd+=720
    if endHour==12:
        totalEnd+=endMinute
    else:
        totalEnd+=endHour*minInHour+endMinute

    minDiff=totalEnd-totalStart
    
    if minDiff<0:
        dayMinLength=1440
        return minDiff+1440
    return minDiff

if __name__=='__main__':
    main()
