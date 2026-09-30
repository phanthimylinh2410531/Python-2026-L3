import math
from domains.student import Student
from domains.course import Course

def input_students(stdscr, students):
    stdscr.clear()
    stdscr.addstr("The number of students in a class: ")
    num = int(stdscr.getstr().decode('utf-8'))

    for _ in range(num):
        stdscr.addstr("Student ID: ")
        s_id = stdscr.getstr().decode('utf-8')
        stdscr.addstr("Student Name: ")
        name = stdscr.getstr().decode('utf-8')
        stdscr.addstr("Date of Birth: ")
        dob = stdscr.getstr().decode('utf-8')

        students.append(Student(s_id, name, dob))

def input_courses(stdscr, courses):
    stdscr.clear()
    stdscr.addstr("The number of courses: ")
    num = int(stdscr.getstr().decode('utf-8'))

    for _ in range(num):
        stdscr.addstr("Course ID: ")
        c_id = stdscr.getstr().decode('utf-8')
        stdscr.addstr("Course Name: ")
        name = stdscr.getstr().decode('utf-8')
        stdscr.addstr("The number of credits: ")
        credits = int(stdscr.getstr().decode('utf-8'))

        courses[c_id] = Course(c_id, name, credits)

def input_marks(stdscr, students, courses):
    for c_id, course in courses.items():
        stdscr.clear()
        stdscr.addstr(f"Mark for: {course.name} ({c_id})\n\n")
        for s in students:
            stdscr.addstr(f"Marks of student {s.name}: ")
            raw_mark = float(stdscr.getstr().decode('utf-8'))

            rounded_mark = math.floor(raw_mark * 10) / 10
            s.marks[c_id] = rounded_mark