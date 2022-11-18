from unicodedata import name
from student import Student
import datetime
def main():
    runner()

def runner():
    studentList=[]
    studentID=[]
    while True:
        print('Please select from one of the options: ')
        print('1. Quit (exit the program) ')
        print("2. Add Entry to a student file")
        print("3. Output information of all Students")
        print("4. Compute and output the average overall mark for students currently held in the list/ array")
        print("5. Detirmine and display how many students obtained an overall mark equal to or above the average overall mark and how many obtained an overall mark below the average overall mark")
        print("6. Display distribution of grades")
        print("7. Given student number (ID), view all details of student with that number")
        print("8. Given a student's name (both surname and given name-ignoring case, view all details of that student. If the student is not found error message will be displayed")
        print("9.Sort the list/array of student objects into ascending order of student's numbers ")
        choice=input('Enter an option: ')
        match choice:
            case '1':
                break
            case '2':
                add_fxn(studentList,studentID)
            case '3':
                output_fxn(studentList)
            case '4':
                compute_avg_fxn(studentList,'y')
            case '5':
                student_distribution(studentList)
            case '6':
                None
            case '7':
                find_id_fxn(studentList)
            case '8':
                find_name_fxn(studentList)
            case '9':
                my_sort(studentID)
            case other:
                "Invalid input, please try again."
    
    
    
    
        
    
def add_fxn(nameList,idList):
    first=input('Input first name of student: ') 
    last=input('Enter last name of student: ')   
    stud=Student(first,last) 
    nameList+=[stud]
    stud.set_DOB()
    idList+=[stud.set_id()]
    stud.set_assignment1()
    stud.set_assignment2()
    stud.set_labwork()
    stud.set_exam1()
    stud.set_exam2()
    stud.set_final_exam()
    stud.calc_final_grade()
    stud.calc_overall_mark()

def output_fxn(nameList):
    print('Student Name                  Student ID             Date of Birth       Final Grade         Overall Mark')
    for student in nameList:
        print(student)

def compute_avg_fxn(studList,oper='n'):
    count=0
    finalSum=0
    for student in studList:
        grade=float(student.get_final_grade())
        finalSum+=grade
        count+=1
    averageGrade=finalSum/count 
    if oper=='y': 
        print('The average score for the students is ',round(averageGrade),'%')
    return averageGrade  

def student_distribution(studList):
    countBelow=0
    countAbove=0
    N=0
    P=0
    C=0
    D=0
    HD=0
    for student in studList:
        grade=student.get_overall_mark()
        match grade:
            case 'N':
                N+=1
            case 'P':
                P+='1'
            case 'C':
                C+=1
            case 'D':
                D+=1
            case 'HD':
                HD+=1
    midgrade=compute_avg_fxn(studList)
    if midgrade<50:
        averageMark='N'
        countBelow=0
        countAbove=P+C+D+HD
    elif midgrade<60:
        averageMark='P'
        countBelow=N
        countAbove=C+D+HD
    elif midgrade<70:
        averageMark='C'
        countBelow=N+P
        countAbove=D+HD
    elif midgrade<80:
        averageMark='D'
        countBelow=N+P+C
        countAbove=HD
    else:
        averageMark='HD'
        countBelow=N+P+C+D
        countAbove=0
    print('The average overall mark was ',averageMark,' The amount of students scored below the average mark is ',countBelow,'. The amount of students who scored above the average mark is ',countAbove)
        

    

def find_id_fxn(studList):
    id=input('Enter student ID: ')
    for student in studList:
        if student.id==id:
            print(student)
            return None
    print('No such student with id ',id,' exists.')

def find_name_fxn(studList):
    name=input('Enter first or last name of student: ').lower()
    found='n'
    for student in studList:
        if name==student.firstName.lower() or name==student.lastName.lower():
            found='y'
            print(student)
    if found=='n':
        print('No student with name' , name, 'found')


def my_sort(idList):
    sortedArray=[]
    for id in idList:
        fit='n'
        head=0
        tail=len(sortedArray)-1
        if len(sortedArray)==0:
            sortedArray=[id]
            fit='y'                
        while fit=='n':
            if id<=sortedArray[0]:
                sortedArray=[id]+sortedArray
                fit='y'
            elif id>=sortedArray[-1]:
                sortedArray=sortedArray+[id]
                fit='y'
            elif sortedArray[head+1]>=id>=sortedArray[head]:
                sortedArray=sortedArray[:head+1]+[id]+sortedArray[head+1:]
                fit='y'
            elif sortedArray[tail]>=id>=sortedArray[tail-1]:
                sortedArray=sortedArray[:tail]+[id]+sortedArray[tail:]
                fit='y'
            else:
                head+=1
                tail-=1
                    
                
    return sortedArray  
    


if __name__=='__main__':
    main()

