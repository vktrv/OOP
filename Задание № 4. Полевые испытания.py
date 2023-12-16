class Mentor:
    #создаём список преподователей :
    mentor_list = []
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = [] #подключенные курсы
        self.grades_dict_lecturer = {} #словарь с оценками лекторам от студентов
        self.average_grade = 0 #средняя оценка за лекции
        self.mentor_list.append(self) #добавим в список преподователей вновь созданный экземпляр

class Student:
    #создадим общий список студентов
    student_list = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.student_list.append(self) #добавим в список студентов вновь созданный экземпляр
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
        #подсчитаем сумму оценок
        sum_ = sum(grade_list)
        #подсчитаем среднее значение всех оценок
        self.average_grade = round(sum_/len(grade_list), 2)
        return self.average_grade

    #метод выставления оценок студентами лекторам
    def add_grades_lecturer(self, lecturer, course, grades):
        #если лектор - экземпляр класса Lecturer , курс входит в список курсов ,которые ведёт лектор и курс входит в список текущих курсов студента , то
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
                and course in self.courses_in_progress:
            if course in lecturer.grades_dict_lecturer:
                lecturer.grades_dict_lecturer[course] += [grades]
            else:
                lecturer.grades_dict_lecturer[course] = [grades]
        else:
            print(f'Ошибка. Проверьте , является ли  {lecturer.name} {lecturer.surname} экземпляром'
                  f' класса Student , входит ли "{course}" в список курсов , которые на данный момент'
                  f' изучает студент {lecturer.name} {lecturer.surname} '
                  f' и  является ли "{course}" - курсом , на котором преподаёт'
                  f' {self.name} {self.surname}')

    #метод __str__ для Student
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
        sum_ = sum(grade_list)
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
            print(f'Ошибка. Проверьте , является ли  {student.name} {student.surname} экземпляром'
                  f' класса Student , входит ли "{course}" в список курсов , которые на данный момент'
                  f' изучает студент {student.name} {student.surname} '
                  f' и  является ли "{course}" - курсом , на котором преподаёт'
                  f' {self.name} {self.surname}')
    #метод __str__ для Reviewer :
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия = {self.surname}'
        return res

    # функция для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
    #(в качестве аргументов принимаем список студентов и название курса)
    def get_average_grade_student_course(other_list, course):
        #создаём пустой список оценок всех студентов конкретного курса
        all_grades_list_course = []
        for student in other_list:
            for key, vul in student.grades_dict_student.items():
                if key == course:
                    #добавим в общий список оценок оценки конкретного студента
                    all_grades_list_course.extend(vul)
        #сумма всех оценок студентов данного курса
        sum_ = sum(all_grades_list_course)
        #средняя оценка
        average_grade_student = round(sum_ / len(all_grades_list_course), 2)
        return average_grade_student

    #функция для подсчета средней оценки за лекции всех лекторов в рамках курса (в качестве аргумента
    #принимаем список лекторов и название курса)
    def get_average_grade_mentor_course(other_list, course):
        #вызываем список курсов лекторов
        lecturer_course_list = get_lecturer_course(other_list)
        #проверяем, входит ли подаваемый на вход функции курс в список курсов лекторов
        if course not in lecturer_course_list:
            print('Ошибка.Такого курса нет в списке курсов лекторов')
            return
        all_grades_lecturer_course = []  #список оценок лекторов
        for lecturer in other_list:
            if len(lecturer.grades_dict_lecturer) > 0:
                for key, vul in lecturer.grades_dict_lecturer.items():
                    if key == course:
                        all_grades_lecturer_course.extend(vul)  #заполняем список оценок лекторов
        #сумма всех оценок лекторов данного курса
        sum_ = sum(all_grades_lecturer_course)
        #средняя оценка
        average_grade_lecturer = round(sum_ / len(all_grades_lecturer_course), 2)
        return average_grade_lecturer