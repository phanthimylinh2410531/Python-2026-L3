import curses
import os
import zipfile
import input as inp
import output as out

def compress_and_cleanup():
    files_to_compress = ["students.txt", "courses.txt", "marks.txt"]

    with zipfile.ZipFile('students.dat', 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in files_to_compress:
            if os.path.exists(file):
                zipf.write(file)
                os.remove(file)

def main(stdscr):
    curses.echo()

    students = []
    courses = {}

    is_loaded = inp.load_data(students, courses)

    if not is_loaded:
        inp.input_students(stdscr, students)
        inp.input_courses(stdscr, courses)
        inp.input_marks(stdscr, students, courses)
    else:
        stdscr.clear()
        stdscr.addstr("Data loaded from students.dat!\n")
        stdscr.addstr("Press any key to continue.")
        stdscr.getch()

    out.list_students_and_gpa(stdscr, students, courses)
    compress_and_cleanup()

if __name__ == "__main__":
    curses.wrapper(main)