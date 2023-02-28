from Student import *

ds = []

def addStudent():
    id = input("Enter the id: ")
    name = input("Enter the name: ")
    sv = Student(id,name)
    ds.append(sv)

def updateStudent():
    id = input("Enter id need update: ")
    for i in ds:
        if i.get_id() == id:
            i.set_name(input("Enter name need fix: "))
            i.show_info()

def viewStudent():
    if len(ds) == 0:
        print("Persent student not exist list")
    else:
        print(f"Present {len(ds)} Student")
        for i in ds:
            i.show_info()

def numberStudent():
    print(f"Persent {len(ds)} student")

def searchStudentId():
    id = input("Enter id need search: ")
    if len(ds) == 0:
        print("Id student is not exist")
    else:
        for i in ds:
            if i.get_id() == id:
                i.show_info()

def searchStudentName():
    name = input("Enter name need search: ")
    if len(ds) == 0:
        print("Name student is not exist")
    else:
        for i in ds:
            if i.get_name() == name:
                i.show_info()

def removeStudent():
    name = input("Enter a username remove: ")
    if len(ds) == 0:
        print("Name student no exist.")
    else:
        for i in ds:
            if i.get_name() == name:
                ds.remove(i)


    