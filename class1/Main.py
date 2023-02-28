from ManageStudent import *
import ManageStudent as sv

while True:
    print("""
    ~~~~~~~~~~~~~~~~~~~~~~
    1. addStudent
    2. updateStudent
    3. viewStudent
    4. numberStudent
    5. searchStudentID
    6. searchStudentName
    7. removeStudent
    0. exist
    ~~~~~~~~~~~~~~~~~~~~~~~
    """)
    select = int(input("Enter a number: "))
    if select == 1:
        sv.addStudent()
    elif select == 2:
        sv.updateStudent()
    elif select == 3:
        sv.viewStudent()
    elif select == 4:
        sv.numberStudent()
    elif select == 5:
        sv.searchStudentId()
    elif select == 6:
        sv.searchStudentName()
    elif select == 7:
        sv.removeStudent()
    elif select == 0:
        break
    else:
        print("Number not True.")
    
        
        
    