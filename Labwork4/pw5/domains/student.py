import numpy as np

class Student:
    def __init__(self, s_id, name, dob):
        self.id = s_id
        self.name = name
        self.dob = dob
        self.marks = {}
        self.gpa = 0.0

    def calculate_gpa(self, courses):
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