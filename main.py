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

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Средняя оценка за домашние задания: {calculate_medium(self.grades)}\n" \
               f"Курсы в процессе изучения: {self.courses_in_progress}\n" \
               f"Завершенные курсы: {self.finished_courses}"

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    lector_grades = {}

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Средняя оценка за лекции: {calculate_medium(self.lector_grades)}\n"

class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:

            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


def calculate_medium(grades):

    all_summ = 0
    count = 0
    for grade_list in grades.values():
        all_summ += sum(grade_list)
        count += len(grade_list)
    return all_summ / count


lecturer_1 = Lecturer('Some', 'Buddy')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['JS']

reviewer_1 = Reviewer('SomeR', 'BuddyR')
reviewer_1.courses_attached += ['Python']

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['JS']

reviewer_1.rate_hw(best_student, 'Python', 10)
reviewer_1.rate_hw(best_student, 'Python', 9)
reviewer_1.rate_hw(best_student, 'Python', 9)
print(f"{best_student.grades}\n")

best_student.finished_courses += ['Введение в программирование']
best_student.rate_for_lec(lecturer_1, 'Python', 8)
best_student.rate_for_lec(lecturer_1, 'Python', 10)
best_student.rate_for_lec(lecturer_1, 'JS', 2)
print(f"{lecturer_1.lector_grades}\n")

print(f"{reviewer_1}\n")
print(f"{lecturer_1}\n")
print(f"{best_student}\n")