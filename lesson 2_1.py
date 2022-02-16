class Person:
    def __init__(self, fullname, age, is_married):
        self.full = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f"Fullname:{self.full}\n"
              f"age: {self.age}\n"
              f"is married: {self.is_married}")


people = Person('Nat', 19, False)
print(people.introduce_myself())


class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def grade(self):
        return sum(self.marks.values())//len(self.marks)

d = Student('Nat', 19, False, marks={'русский':5,'english':5,'физика':5,'алгебра':5})
print(d.grade())

class Teacher(Person):

    salary = 20000

    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def __str__(self):
        return super(Teacher, self).introduce_myself()+f"\nexperience: {self.experience}"

    def calculate(self):
        if self.experience > 3:
            s = (self.salary + ((self.salary * 0.05) * (self.experience - 3)))
            return s
        return self.salary

t = Teacher('teacher', 30, True, 10)
print(t.calculate())

def create_students():
    d2 = Student('Nat', 19, False, marks={'русский': 5, 'english': 5, 'физика': 5, 'алгебра': 5})
    d3 = Student('uytvytv', 19, False, marks={'русский': 5, 'english': 5, 'физика': 5, 'алгебра': 5})
    d4 = Student('ibibi', 19, False, marks={'русский': 5, 'english': 5, 'физика': 5, 'алгебра': 5})

    return [f"name: {d2.full}", f"grade: {d2.grade()}",
            f"name: {d3.full}", f"grade:{d3.full}",
            f"name: {d4.full}", f"grade: {d4.grade()}"]

test1 = create_students()
print(test1)

for func in {create_students}:
    x = func()
    print(x)