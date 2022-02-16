
from datetime import datetime
from random import choice

asket_studenst = []


studenst = [
    {2: 'Edil'},
    {3: 'Amantur'},
    {4: 'Aman'},
    {6: 'Yryskeldi'},
    {7: 'Amantur'},
    {11: 'Ismet'},
    {12: 'Diliar'},
    {13: 'syrgabek'},
]

c = len(studenst)
while c !=0:
    c -=1
    random_studenst = studenst.index(choice(studenst))
    print(random_studenst)
    print(studenst[random_studenst])
    print(studenst)
    rate = int(input(f'пастафьте отценку: от 1 до 10 {studenst[random_studenst]}: '))
    studenst[random_studenst].update(dict(rate=rate ))
    asket_studenst.appant(studenst.pop(random_studenst))
    print(asket_studenst)
        file
