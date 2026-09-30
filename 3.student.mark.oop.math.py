import math
import numpy as np
import curses

students = []
courses = {}

class Student:
    def __init__(self, s_id, name, dob):
        self.id = s_id
        self.name = name
        self.dob = dob
        self.marks = {}
        self.gpa = 0.0

    def calculate_gpa(self):
        marks_list = []
        credits_list = []

        for c_id, mark in self.marks.items():
            marks_list.append(mark)
            credits_list.append(courses[c_id].credits)

        if not marks_list:
            return 0.0

        np_marks = np.array(marks_list)
        np_credits = np.array(credits_list)

        self.gpa = np.sum(np_marks * np_credits) / np.sum(np_credits)
        return self.gpa

class Course:
    def __init__(self, c_id, name, credits):
        self.id = c_id
        self.name = name
        self.credits = credits

def input_students(stdscr):
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

def input_courses(stdscr):
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

def input_marks(stdscr):
    for c_id, course in courses.items():
        stdscr.clear()
        stdscr.addstr(f"Mark for: {course.name} ({c_id})\n\n")
        for s in students:
            stdscr.addstr(f"Marks of student {s.name}: ")
            raw_mark = float(stdscr.getstr().decode('utf-8'))

            rounded_mark = math.floor(raw_mark * 10) / 10
            s.marks[c_id] = rounded_mark 

def list_students_and_gpa(stdscr):
    stdscr.clear()

    for s in students:
        s.calculate_gpa()

    students.sort(key=lambda s: s.gpa, reverse = True)

    stdscr.addstr("List of Student with GPA descending\n\n")
    for s in students:
        stdscr.addstr(f"ID: {s.id} | Name: {s.name} | DoB: {s.dob} | GPA: {s.gpa: .1f}\n")

    stdscr.addstr("\nEnd the program.")
    stdscr.getch()
    
def main(stdscr):
    curses.echo()

    input_students(stdscr)
    input_courses(stdscr)
    input_marks(stdscr)
    list_students_and_gpa(stdscr)

if __name__ == "__main__":
    curses.wrapper(main)