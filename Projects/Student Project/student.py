import datetime

class Student:
    def __init__(self,firstName,lastName):
        self.firstName=firstName
        self.lastName=lastName
        self.nameCheck()
        
    def nameCheck(self):
        if not self.firstName.isalpha() or not self.lastName.isalpha() or len(self.firstName)<=2 or len(self.lastName)<=2:
            print('Invalid Entry')
            self.firstName=input('Enter a first name: ')
            self.lastName=input('Enter a last name: ')
            self.nameCheck()
        else:
            self.firstName=self.firstName.capitalize()
            self.lastName=self.lastName.capitalize()

        
    
    def set_id(self):
        self.id=input("Enter an id: ")
        if not self.id.isnumeric():
            print('ID must be only numbers')
            self.id=self.set_id()
        return int(self.id)
        
    
    def set_DOB(self):
        self.DOB=input("Enter a date of birth (DD/MM/YYYY)")
        try:
            datetime.datetime.strptime(self.DOB, '%d/%m/%Y')
        except ValueError:
            print('Invalid entry, please enter in DD/MM/YYY format')
            self.set_DOB()

    def check_score(self,x,lab='n'):
        try:
            z=float(x)
            if (z<0 or z>100) and lab=='n' :
                return 'invalid'
            elif (z<0 or z>10) and lab=='y':
                return 'invalid'

            return z
        except:
            return 'invalid'

    def set_assignment1(self):
        self.assignment1=input('Enter first assignment score (0-100) : ')
        self.assignment1=self.check_score(self.assignment1)
        if self.assignment1=='invalid':
            print('Invalid entry')
            self.assignment1=self.set_assignment1()
        return self.assignment1
    
    def set_assignment2(self):
        self.assignment2=input('Enter second assignment score (0-100) : ')
        self.assignment2=self.check_score(self.assignment2)
        if self.assignment2=='invalid':
            print('Invalid entry')
            self.assignment2=self.set_assignment2()
        return self.assignment2
    
    def set_labwork(self):
        self.lab=input('Enter lab work grade (0-10) : ')
        self.lab=self.check_score(self.lab,'y')
        if self.lab=='invalid':
            print('Invalid entry')
            self.lab=self.set_labwork()
        return self.lab

            

    def set_exam1(self):
        self.exam1=input('Enter first exam score (0-100) : ')
        self.exam1=self.check_score(self.exam1)
        if self.exam1=='invalid':
            print('Invalid entry')
            self.exam1=self.set_exam1()
        return self.exam1

    def set_exam2(self):
        self.exam2=input('Enter second exam score (0-100) : ')
        self.exam2=self.check_score(self.exam2)
        if self.exam2=='invalid':
            print('Invalid entry')
            self.exam1=self.set_exam2()
        return self.exam2
        
    def set_final_exam(self):
        self.final=input('Enter final exam score (0-100) : ')
        self.final=self.check_score(self.final)
        if self.final=='invalid':
            self.final=self.set_final_exam()
        return self.final

    def calc_final_grade(self):
        finalWeight,finalMax=.5,100
        assignmentWeight,assignmentMax=.4,200
        labWeight,labMax=.1,10
        final=(finalWeight*self.final/finalMax)*100
        assignment=(assignmentWeight*(self.assignment1+self.assignment2)/assignmentMax)*100
        lab=(labWeight*self.lab/labMax)*100
        self.finalGrade=final+assignment+lab
    
    def get_final_grade(self):
        return str(self.finalGrade)

    def calc_overall_mark(self):
        if self.finalGrade>=80:
            self.mark='HD'
        elif self.finalGrade>=70:
            self.mark='D'
        elif self.finalGrade>=60:
            self.mark='C'
        elif self.finalGrade>=50:
            self.mark='P'
        else:
            self.mark='N'

    def get_overall_mark(self):
        return self.mark

    def __str__(self):
        
        firstSpace=len('Student Name                  ')-(len(self.firstName)+len(self.lastName))
        secondSpace=len('tudent ID               ')-len(str(self.id))
        thirdSpace=len('Date of Birth         ')-len(self.DOB)
        fourthSpace=len('Final Grade             ')-len(str(self.finalGrade))
        return str(self.firstName)+' '+str(self.lastName)+' '*(firstSpace)+str(self.id)+' '*secondSpace+str(self.DOB)+' '*thirdSpace+str(round(self.finalGrade))+' '*fourthSpace+str(self.mark)
        
            



        