class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = [] #подключенные курсы
        self.grades_dict_lecturer = {} #словарь с оценками лекторам от студентов
        self.average_grade = 0 #средняя оценка за лекции


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = [] #изучаемые на данный момент курсы
        self.grades_dict_student = {} #словарь с оценками студентов от проверяющих
        self.average_grade = 0 #средняя оценка за ДЗ

        #метод для добавления пройденных курсов
    def add_courses (self, course_name):
        self.finished_courses.append(course_name)

        #метод вычисления средней оценки за ДЗ
    def average_grade_student(self):
        grade_list = []
        for val in self.grades_dict_student.values():
            grade_list.extend(val)
        #подсчитаем сумму оценок:
        sum_ = sum(grade_list)
        #подсчитаем среднее значение всех оценок
        self.average_grade = round(sum_/len(grade_list), 2)
        return self.average_grade

    #метод выставления оценок студентами лекторам
    def add_grades_lecturer(self, lecturer, course, grades):
        #если лектор - экземпляр класса Lecturer , курс входит в список курсов ,которые ведёт лектор и курс входит в список текущих курсов студента
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
                and course in self.courses_in_progress:
            if course in lecturer.grades_dict_lecturer:
                lecturer.grades_dict_lecturer[course] += [grades]
            else:
                lecturer.grades_dict_lecturer[course] = [grades]
        else:
            print(f'Ошибка. Проверте , является ли  {lecturer.name} {lecturer.surname} экземпляром'
                  f' класса Student , входит ли "{course}" в список курсов , которые на данный момент'
                  f' изучает студент {lecturer.name} {lecturer.surname} '
                  f' и  является ли "{course}" - курсом , на котором преподаёт'
                  f' {self.name} {self.surname}')

    #метод __str__ для Student :
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия : {self.surname}\nСредняя ' \
              f'оценка за ДЗ: {self.average_grade_student()}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return res

    #метод сравнения средних оценок студентов:
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.average_grade < other.average_grade


#дочерние для класса Mentor классы Lecturer (лекторы) и Reviewer (проверяющие)
class Lecturer(Mentor):

    #метод вычисления средней оценки за лекции
    def average_grade_lectures(self):
        grade_list = []
        for val in self.grades_dict_lecturer.values():
            grade_list.extend(val)
        #подсчитаем сумму оценок
        sum_ =sum (grade_list)
        #подсчитаем среднее значение всех оценок
        self.average_grade = round(sum_/len(grade_list), 2)
        return self.average_grade

    #метод сравнения средних оценок лекторов
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.average_grade < other.average_grade


    #метод __str__ для Lecturer
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия : {self.surname}\nСредняя ' \
              f'оценка за лекции: {self.average_grade_lectures()}'
        return res


class Reviewer(Mentor):
    #метод, который позволяет проверяющему добавить оценку в словарь студента по названию курса
    def add_grades_student(self, student, course, grades):
        if isinstance(student, Student) and course in self.courses_attached \
                and course in student.courses_in_progress:
            if course in student.grades_dict_student:
                student.grades_dict_student[course] += [grades]
            else:
                student.grades_dict_student[course] = [grades]
        else:
            print(f'Ошибка. Проверте , является ли  {student.name} {student.surname} экземпляром'
                  f' класса Student , входит ли "{course}" в список курсов , которые на данный момент'
                  f' изучает студент {student.name} {student.surname} '
                  f' и  является ли "{course}" - курсом , на котором преподаёт'
                  f' {self.name} {self.surname}')


    #метод __str__ для Reviewer
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия = {self.surname}'
        return res