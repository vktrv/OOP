class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades_dict_lecturer = {} #словарь с оценками лекторам от студентов

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades_dict_student = {}  #оценки

        #метод для добавления пройденных курсов
        def add_courses(self, course_name):
            self.finished_courses.append(course_name)

        #метод выставления оценок студентами лекторам
        def add_grades_lecturer(self, lecturer, course, grades):
            #если лектор - экземпляр класса Lecturer , курс входит в список курсов ,которые ведёт лектор и курс входит в список текущих курсов студента :
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


#создаём дочерние для класса Mentor классы Lecturer (лекторы) и Reviewer
class Lecturer(Mentor):
    pass


class Reviewer(Mentor):
    #метод, который позволяет добавить оценку проверяющим в словарь студента по названию курса
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


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.add_grades_student(best_student, 'Python', 10)
cool_reviewer.add_grades_student(best_student, 'Python', 10)
cool_reviewer.add_grades_student(best_student, 'Python', 10)

print(best_student.grades_dict_student)
