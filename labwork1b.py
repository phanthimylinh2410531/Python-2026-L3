students = []
courses = []
marks = {}

def input_students():
    number_students = int(input("The number of students in a class : "))
    for i in range(number_students):
        s_id = input("Student ID : ")
        s_name = input("Student Name : ")
        dob = input("Date of Birth : ")
        students.append({"ID" : s_id, "Name" : s_name, "DoB" : dob})

def input_courses():
    number_courses = int(input("The number of courses : "))
    for i in range(number_courses):
        c_id = input("Course ID : ")
        c_name = input("Course Name : ")
        courses.append({"ID" : c_id, "Name" : c_name})

def input_marks():
    c_id = input("Course ID ? ")
    marks[c_id] = {}
    for s in students:
        Marks = float(input(f"Marks of student {s['Name']}: "))
        marks[c_id][s['ID']] = Marks

def list_students():
    print("\n List of Students")
    for s in students :
        print(f"ID: {s['ID']} | Name: {s['Name']} | DoB: {s['DoB']}")

def list_courses():
    print("\n List of Courses")
    for c in courses :
        print(f"ID: {c['ID']} | Name: {c['Name']}")

def show_marks():
    c_id = input("\n Course ID: ")
    print("\n Marks")
    for s in students:
        s_mark = marks[c_id].get(s['ID'], None)
        print(f"{s['Name']} : {s_mark}")

print("Step 1 : Input Functions")
input_students()
input_courses()

print("Step 2 : Marks")
input_marks()

print("Step 3 : Review")
list_students()
list_courses()
show_marks()