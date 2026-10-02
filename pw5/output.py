def list_students_and_gpa(stdscr, students, courses):
    stdscr.clear()

    for s in students:
        s.calculate_gpa(courses)

    students.sort(key=lambda s: s.gpa, reverse = True)

    stdscr.addstr("List of Student with GPA descending\n\n")
    for s in students:
        stdscr.addstr(f"ID: {s.id} | Name: {s.name} | DoB: {s.dob} | GPA: {s.gpa: .1f}\n")

    stdscr.addstr("\nEnd the program.")
    stdscr.getch()