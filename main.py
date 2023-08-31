class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_for_lec(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:

            if course in lector.lector_grades:
                lector.lector_grades[course] += [grade]
            else:
                lector.lector_grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



class Lecturer(Mentor):
    lector_grades = {}

class Reviewer(Mentor):
    # def __init__(self, name, surname):


    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:

            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

lecturer_1 = Lecturer('Some', 'Buddy')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['JS']

reviewer_1 = Reviewer('SomeR', 'BuddyR')
reviewer_1.courses_attached += ['Python']

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['JS']


# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']

reviewer_1.rate_hw(best_student, 'Python', 10)
reviewer_1.rate_hw(best_student, 'Python', 10)
reviewer_1.rate_hw(best_student, 'Python', 10)
print(best_student.grades)

best_student.rate_for_lec(lecturer_1, 'Python', 8)
best_student.rate_for_lec(lecturer_1, 'Python', 10)
best_student.rate_for_lec(lecturer_1, 'JS', 2)
print(lecturer_1.lector_grades)