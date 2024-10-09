def Print(students):
    for student in students:
        print(f"Group number: {student['group_number']}")
        print(f"Full name: {student['full_name']}")
        print(f"Course: {student['course']}")
        print("Subjects and grades:")
        for subject, grade in student["subjects"].items():
            print(f"  - {subject}: {grade}")
        print()

def add_student(students_list, new_student):
    students_list.append(new_student)
    Print(students)

students = [
    {
        "group_number": "КН-33",
        "full_name": "Baranov Erik Vitaliyovych",
        "course": 3,
        "subjects": {
            "Algorithms and data structures": 85,
            "MMDO": 90,
            "Python programming": 88,
            "Numerical methods": 75
        }
    },
    {
        "group_number": "КН-31",
        "full_name": "Kuchma Petro Dorianovych",
        "course": 1,
        "subjects": {
            "Algorithms and data structures": 75,
            "MMDO": 51,
            "Python programming": 93,
            "Numerical methods": 66
        }
    },
    {
        "group_number": "КН-32",
        "full_name": "Poroh Kate Mykolaivna",
        "course": 2,
        "subjects": {
            "Algorithms and data structures": 77,
            "MMDO": 98,
            "Python programming": 78,
            "Numerical methods": 85
        }
    },
    {
        "group_number": "КН-34",
        "full_name": "Raven Arnold Adolfovich",
        "course": 1,
        "subjects": {
            "Algorithms and data structures": 61,
            "MMDO": 79,
            "Python programming": 80,
            "Numerical methods": 92
        }
    },
    {
        "group_number": "КН-35",
        "full_name": "Stark Ermund Adamovych",
        "course": 4,
        "subjects": {
            "Algorithms and data structures": 88,
            "MMDO": 95,
            "Python programming": 79,
            "Numerical methods": 97
        }
    },
 ]  

new_student = {
 "group_number": "КН-37",
 "full_name": "Wise Olga Yaroslavivna",
 "course": 3,
 "subjects": {
     "Algorithms and data structures": 91,
     "MMDO": 95,
     "Python programming": 97,
     "Numerical methods": 99
 }
}

def case1():
    return Print(students)

def case2():
    return add_student(students, new_student)

def default():
    return "Wrong number"

switch = {
    1: case1,
    2: case2,
}

print("Enter a number 1, if you want print of vocabulary;")
print("Enter a number 2, if you want to add new student;")
option = int(input("Enter a number (1-2): "))
switch.get(option, default)()

#       ↑
#Duzhak Ivan KN-33-1