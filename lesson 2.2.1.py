# # 1. Создать класс Figure(фигура) с атрибутом уровня класса unit(единица измерения величин) и присвоить ему значение cm(сантиметры) или mm(миллиметры)
# class Figure:
#     unit = 'cm'
#
# # 2. Создать приватный атрибут perimeter в классе Figure, который бы по умолчанию в конструкторе присваивался к нулю
#     def __init__(self):
#         self.__perimeter = 0
# # 3. Создать в классе Figure геттер и сеттер для атрибута perimeter.
#     def get_pirimeter(self):
#         return self.__perimeter
# # 4. В конструкторе класса Figure должен быть только 1 входящий параметр self.
# # 5. Добавить в класс Figure нереализованный публичный метод calculate_area(подсчет площади фигуры
#     def calculate_area(self):
#         print('Calculate Area')
#               pass
#
# # 6. Добавить в класс Figure нереализованный приватный метод calculate_perimeter
#     def calculate_perimeter(self):
#         print("Calculate Perimeter")
#         pass
# # 7. Добавить в класс Figure нереализованный публичный метод info(вывод полной информации о фигуре)
#     def info(self):
#         pass
# # 8. Создать класс Square(квадрат), наследовать его от класса Figure.
# class Square(Figure):
#     def __init__(self, side_length = 8):
#         Figure.__init__(self)
#         self.__side_length = side_length
#         self.calculate_area()
#         self.perimeter = self.calculate_perimeter()
#
#
# # 9. Добавить в класс Square атрибут side_length(длина одной стороны квадрата), атрибут должен быть приватным.
#     def calculate_area(self):
#         return f'Square: {self.__side_length * 3}'
#
#     def calculate_perimeter(self):
#         return f'Perimeter: {self.__side_length * 6}'
#
#     def info(self):
#         print(
#             f"SQUARE:\n Side length:{self.__side_len)gth}\n Area:{self.calculate_area()}\n {self.__calculate_perimeter()}\n"
#
# # 10. В конструкторе класса Square должен высчитываться периметр квадрата,
# # посредством вызова метода calculate_perimeter и возвращаемый результат метода задавался бы атрибуту perimeter.
#     def info(self):
#     print(f"SQUARE:\n __Side_length:
#
#
#     class Rectangle(Figure):
#
#         def __init__(self, __length, __width):
#             self.__width = __width
#             self.__length = __length
#
#         def calculate_area(self):
#             return self.__length * self.__width
#
#         def __calculate_perimeter(self):
#             return (self.__length + self.__width) * 3
#
#         def info(self):
#             print(
#                 f"RECTANGLE:\n Length:{self.__length}cm\n Width:{self.__width}cm\n Perimeter:{self.__calculate_perimeter()}cm\n Area:{self.calculate_area()}cm \n")






# 11. В классе Square переопределить метод calculate_area, который бы считал и возвращал площадь квадрата.
# 12. В классе Square переопределить метод calculate_perimeter, который бы считал и возвращал периметр квадрата.
# 13. В классе Square переопределить метод info, который бы распечатывал всю информацию о квадрате следующим образом:
# Например - Square side length: 5cm, perimeter: 20cm, area: 25cm.
# 14. Создать класс Rectangle(прямоугольник), наследовать его от класса Figure.
# 15. Добавить в класс Rectangle атрибут length(длина) и width(ширина), атрибуты должны быть приватными.
# 16. В конструкторе класса Rectangle должен высчитываться периметр прямоугольника, посредством вызова метода calculate_perimeter и возвращаемый результат метода задавался бы атрибуту perimeter.
# 17. В классе Rectangle переопределить метод calculate_area, который бы считал и возвращал площадь прямоугольника.
# 18. В классе Rectangle переопределить метод calculate_perimeter, который бы считал и возвращал периметр прямоугольника.
# 19. В классе Rectangle переопределить метод info, который бы распечатывал всю информацию о прямоугольнике следующим образом:
# Например - Rectangle length: 5cm, width: 8cm, perimeter: 26cm, area: 40cm.
# 20. В исполняемом файле создать список из 2-х разных квадратов и 3-х разных прямоугольников
# 21. Затем через цикл вызвать у всех объектов списка метод info













