def compare(self, some_other):

    if isinstance(some_other, Student) or isinstance(some_other, Lecturer):

        self_grades = calculate_medium([self])
        some_other_grades = calculate_medium([some_other])

    else:
        return 'Ошибка'

    if self_grades == some_other_grades:
        print(f"Оценки {self.name} {self.surname} и {some_other.name} {some_other.surname} равны: {self_grades} = {some_other_grades}")

    elif self_grades > some_other_grades:
        print(f"{self.name} {self.surname} победил: {self_grades} > {some_other_grades}")

    else:
        print(f"{some_other.name} {some_other.surname} победил: {self_grades} < {some_other_grades}")


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

            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'


    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Средняя оценка за домашние задания: {calculate_medium([self])}\n" \
               f"Курсы в процессе изучения: {self.courses_in_progress}\n" \
               f"Завершенные курсы: {self.finished_courses}\n"

    compare_students = compare

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Средняя оценка за лекции: {calculate_medium([self])}\n"


    compare_lectors = compare

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


def calculate_medium(instances_list, course_name = ""):

    all_summ = 0
    count = 0
    for instance in instances_list:
        for grade_key, grade_value in instance.grades.items():
            if course_name == "" or course_name == grade_key:
                all_summ += sum(grade_value)
                count += len(grade_value)
    if count == 0:
        return 0
    else:
        return all_summ / count


# лекторы
lecturer_1 = Lecturer('Some', 'Buddy')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['JS']

lecturer_2 = Lecturer('Jane', 'Doe')
lecturer_2.courses_attached += ['Python']
lecturer_2.courses_attached += ['Введение в программирование']

# проверяющие
reviewer_1 = Reviewer('Mark', 'Reviewer')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['JS']

reviewer_2 = Reviewer('Sara', 'Connor')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['Введение в программирование']

# студенты
student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['JS']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Hari', 'Krishna', 'your_gender')
student_2.courses_in_progress += ['Python']
student_2.finished_courses += ['Введение в программирование']

# оценка лекторов
student_1.rate_for_lec(lecturer_1, 'Python', 2)
student_1.rate_for_lec(lecturer_1, 'Python', 2)
student_1.rate_for_lec(lecturer_1, 'JS', 2)

student_1.rate_for_lec(lecturer_2, 'Введение в программирование', 10)
student_1.rate_for_lec(lecturer_2, 'Python', 10)
student_1.rate_for_lec(lecturer_2, 'JS', 10)

student_2.rate_for_lec(lecturer_2, 'Python', 10)
student_2.rate_for_lec(lecturer_2, 'JS', 2)
student_2.rate_for_lec(lecturer_2, 'Введение в программирование', 10)

# оценка студентов
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'JS', 5)

reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 9)



print(f"{lecturer_1}\n")
print(f"{lecturer_2}\n")

print(f"{reviewer_1}\n")
print(f"{reviewer_2}\n")

print(f"{student_1}\n")
print(f"{student_2}\n")

# сравнение студентов
print("В сравнении среденй оценки по всем предметам среди студентов")
student_1.compare_students(student_2)

# сравнение лекторов
print("В сравнении среденй оценки по всем предметам среди лекторов")
lecturer_1.compare_lectors(lecturer_2)
print()

# подсчет средней оценки за домашние задания по всем студентам в рамках конкретного курса
course_1 = 'JS'
course_2 = 'Python'

print(f"Средняя оценка студентов в рамках курса {course_1}: {calculate_medium([student_1, student_2], course_1)}")
print(f"Средняя оценка студентов в рамках курса {course_2}: {calculate_medium([student_1, student_2], course_2)}")
print()

print(f"Средняя оценка лекторов в рамках курса {course_1}: {calculate_medium([lecturer_1, lecturer_2], course_1)}")
print(f"Средняя оценка лекторов в рамках курса {course_2}: {calculate_medium([lecturer_1, lecturer_2], course_2)}")
print()