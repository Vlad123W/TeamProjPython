#Функція, яка виводить словник
def Print(students):
    for student in students:
        print(f"Group number: {student['group_number']}")
        print(f"Full name: {student['full_name']}")
        print(f"Course: {student['course']}")
        print("Subjects and grades:")
        for subject, grade in student["subjects"].items():
            print(f"  - {subject}: {grade}")
        print()

#Функція, яка додає до словника нового студента та виводить словник
def add_student(students_list, new_student):
    students_list.append(new_student)
    Print(students)

#Функція, яка створює нового студента
def new_student(group, full_name, course, grade_1, grade_2, grade_3, grade_4):
 new_student = {
 "group_number": group,
 "full_name": full_name,
 "course": course,
 "subjects": {
     "Algorithms and data structures": grade_1,
     "MMDO": grade_2,
     "Python programming": grade_3,
     "Numerical methods": grade_4
 }
}

 return new_student


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

def case1():
    return Print(students)

def case2():
    group = input("Enter the group -> ")
    full_name = input("Enter full name -> ")
    course = int(input("Enter the course -> "))
    grade_1 = int(input("Enter grade 1 -> "))
    grade_2 = int(input("Enter grade 2 -> "))
    grade_3 = int(input("Enter grade 3 -> "))
    grade_4 = int(input("Enter grade 4 -> "))

    return add_student(students, new_student(group, full_name, course, grade_1, grade_2, grade_3, grade_4))

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



#Функція сортування списку за іменами 
def sorting(list):
    return sorted(students, key=lambda student: student['full_name'])

#Функція сортування за середнім балом 
def sort_by_average_grade(students):
    def calculate_average(subjects):
        return sum(subjects.values()) / len(subjects)

    return sorted(students, key=lambda student: calculate_average(student['subjects']))

#Виклик функції сортування за іменами
print("Sorted by name students")

sorting(students)

#Вивід відсортованого списку
Print(students)

#       ↑
#Vlad Konoplenko KN-33-1