import math
import os
import zipfile
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

    with open("students.txt", "w") as f:
        for s in students:
            f.write(f"{s.id},{s.name},{s.dob}\n")

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

    with open("courses.txt", "w") as f:
        for c_id, course in courses.items():
            f.write(f"{course.id},{course.name},{course.credits}\n")

def input_marks(stdscr, students, courses):
    for c_id, course in courses.items():
        stdscr.clear()
        stdscr.addstr(f"Mark for: {course.name} ({c_id})\n\n")
        for s in students:
            stdscr.addstr(f"Marks of student {s.name}: ")
            raw_mark = float(stdscr.getstr().decode('utf-8'))

            rounded_mark = math.floor(raw_mark * 10) / 10
            s.marks[c_id] = rounded_mark

        with open("marks.txt", "w") as f:
            for s in students:
                for c_id, mark in s.marks.items():
                    f.write(f"{s.id},{c_id},{mark}\n")

def load_data(students, courses):
    if not os.path.exists('students.dat'):
        return False

    with zipfile.ZipFile('students.dat', 'r') as zipf:
        zipf.extractall()

    if os.path.exists('students.txt'):
        with open('students.txt', 'r') as f:
            for line in f:
                s_id, name, dob = line.strip().split(',')
                students.append(Student(s_id, name, dob))

    if os.path.exists('courses.txt'):
        with open('courses.txt', 'r') as f:
            for line in f:
                c_id, name, credits = line.strip().split(',')
                courses[c_id] = Course(c_id, name, int(credits))

    if os.path.exists('marks.txt'):
        with open('marks.txt', 'r') as f:
            for line in f:
                s_id, c_id, mark = line.strip().split(',')
                for s in students:
                    if s.id == s_id:
                        s.marks[c_id] = float(mark)
                        break
    return True