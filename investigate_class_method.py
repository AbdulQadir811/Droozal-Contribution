class Student(object):
    number_of_students = 0
    __student_name = 'ali'

    def __init__(self, student_name):
        self.__student_name = student_name
        self.__class__.number_of_students += 1
#       self.set_number_of_students()

    @classmethod
    def get_student_count(cls):
        return cls.number_of_students

    def get_student_name(self):

        return self.__student_name

    @classmethod
    def set_number_of_students(cls):
        cls.number_of_students += 1

    @staticmethod
    def get_school_name():
        school_name = 'MIT'
        return school_name

student_a = Student("A")
assert student_a.get_student_name() == 'A'
student_b = Student("B")
assert student_b.get_student_name() == 'B'
student_c = Student("C")
assert student_c.get_student_name() == 'C'

assert Student.get_student_count() == 3

assert student_a.get_school_name() == 'MIT'
assert student_b.get_school_name() == 'MIT'
assert student_c.get_school_name() == 'MIT'
print Student._Student__student_name
'''        return school_name
student = Student('abdul qadir')
print student.get_student_count()
student = Student('abdul qadir2')
student = Student('abdul qadir3')
print student.get_student_count()
print student.get_student_name()
print student.get_school_name()
print student.get_school_name()
'''
