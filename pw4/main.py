import curses
import input as inp
import output as out

def main(stdscr):
    curses.echo()

    students = []
    courses = {}

    inp.input_students(stdscr, students)
    inp.input_courses(stdscr, courses)
    inp.input_marks(stdscr, students, courses)
    out.list_students_and_gpa(stdscr, students, courses)

if __name__ == "__main__":
    curses.wrapper(main)