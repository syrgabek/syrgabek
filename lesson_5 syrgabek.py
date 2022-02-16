class Rectangle:

    def __init__(self, w, h):
        self.w = w  # ширина
        self.h = h  # длинна

    def __str__(self):
        return "площадь прямоугольника({}x{}) = {}" \
            .format(self.w, self.h, self.square(self.w, self.h))

    @staticmethod
    def square(w, h):
        wh = w * h  # вычисление площади
        return wh


rectangle = Rectangle(4, 8)
print(rectangle)



def menu(breakfast, lunch, diner):
    m = dict(breakfast=breakfast, lunch=lunch, diner=diner)
    return m
#
menu1 = menu('Egg', 'soup', 'carri')
menu2 = menu('porridge','salad','omulet')
menu3 = menu('manta rays','lagman','plof')
print(menu1)
print(menu2)
print(menu3)