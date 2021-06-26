class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def av_grade(self):
        for course, grade in self.grades.items():
            result = {course: sum(grade)/len(grade)}
        return result

    def l_grade(self, lecture, course, grade):
        if isinstance(lecture, Lecture) and course in lecture.courses_attached and course in self.courses_in_progress:
            if course in lecture.grades:
                lecture.grades[course] += [grade]
            else:
                lecture.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        info = f'Имя: {self.name} ' \
               f'\nФамилия: {self.surname} ' \
               f'\nСредняя оценка за домашние задания: {self.av_grade()}' \
               f'\nКурсы в процессе обучения: {self.courses_in_progress}'\
               f'\nЗавершенные курсы: {self.finished_courses}'
        return info

class Lecture(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def av_grade(self):
        for course, grade in self.grades.items():
            result = sum(grade) / len(grade)
        return result

    def __str__(self):
        info = f'Имя: {self.name} ' \
               f'\nФамилия: {self.surname} ' \
               f'\nСредняя оценка за лекции: {self.av_grade()}'
        return info

    def __lt__(self, other):
        if not isinstance(other, Lecture):
            print('Не является лектором!')
            return
        return self.av_grade() < other.av_grade()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)


    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        info = f'Имя: {self.name} \nФамилия: {self.surname}'
        return info


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']


cool_reviewer = Reviewer('Re', 'Viewer')
cool_reviewer.courses_attached += ['Python']


cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

print(best_student.grades)

soso_lecture = Lecture('Lec', 'Ture')
soso_lecture.courses_attached += ['Python']
good_student = Student('Lee', 'Bruce', 'male')
good_student.courses_in_progress += ['Python']
best_student.l_grade(soso_lecture, 'Python', 7)
good_student.l_grade(soso_lecture, 'Python', 6)

print(soso_lecture.grades)

print(cool_reviewer)

print(soso_lecture)

print(best_student)

best_lecture = Lecture('The', 'Best')
best_lecture.courses_attached += ['Python']
best_student.l_grade(best_lecture, 'Python', 9)
good_student.l_grade(best_lecture, 'Python', 10)
print(best_lecture.av_grade())
print(soso_lecture < best_lecture)

print(best_student.av_grade())