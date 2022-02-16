# class Person:
#     def __init__(self, f, a, i):
#         self.fullname = f
#         self.age = a
#         self.is_married = i
#
#     def introduce_yourself(self):
#         return (f'FullName: {self.fullname} \n'
#                 f'Age: {self.age} \n'
#                 f'Married: {self.is_married} ')
#
#
# man = Person('Bakyt_uulu_Amantur', 24, False)
#
#
# # Student
# class Student(Person):
#     def __init__(self, f, a, i, marks):
#         Person.__init__(self, f, a, i)
#         self.marks = marks
#
#     def introduce_yourself(self):
#         return (f'FullName: {self.fullname} \n'
#                 f'Age: {self.age} \n'
#                 f'Married: {self.is_married} ')
#
#     def get_marks(self):
#         return self.marks
#
#
#     def get_am(self):
#         return int(sum(self.marks.values()) / len(self.marks))
#
#
# # {'math': 5}
# st1 = Student('Esen', 13, False, dict(matha=5, physics=5, english=5))
#
#
# class Teacher(Person):
#     salary = 9000
#
#     # конструктор
#     def __init__(self, f, a, i, e):
#         Person.__init__(self, f, a, i)
#         self.experience = e
#
#     def introduce_yourself(self):
#         return (f'FullName: {self.fullname} \n'
#                 f'Age: {self.age} \n'
#                 f'Married: {self.is_married} \n'
#                 f'Experience: {self.experience} ')
#
#     # Метод считывание зарплаты
#     def salary_count(self):
#         if self.experience > 3:
#             return Teacher.salary + (self.experience - 3) * t
#         else:
#             return Teacher.salary
#
#
# #  Call the function
# def create_students():
#     st2 = Student('Aman', 14, False, dict(matha=5, physics=5, english=5))
#     st3 = Student('Oleg', 14, False, dict(matha=3, physics=4, english=5))
#     st4 = Student('Zholon', 14, False, dict(matha=4, physics=4, english=5))
#     return [f'name: {st2.fullname}, Avarege_mark: {st2.get_am()}',
#             f'name: {st3.fullname}, Avarege_mark: {st3.get_am()}',
#             f'name: {st4.fullname}, Avarege_mark: {st4.get_am()}']
#
#
# #  Создаем обьект для класса учитель
# print(man.introduce_yourself())
# print('-' * 40)
# teach1 = Teacher("Aleksey", 37, True, 4)
# t = (Teacher.salary / 100) * 5
# print(st1.introduce_yourself())
# print(st1.get_marks())
# print(f'Avarage mark: {st1.get_am()}')
# print('-' * 40)
# print(teach1.introduce_yourself())
# print(f'Teachers salary: {int(teach1.salary_count())}')
# print('=' * 40)
# for func in [create_students]:
#     x = func()
#     print(x)