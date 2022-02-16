from random import randint
from  datetime import datetime


player = input('введите имя')
o = int(input('количество попыток'))
i = o
start_time = datetime.now()
with open('resylst.txt', 'a', encoding='UTF-8')as  file:
    while o != 0:
        try:
            n1, n2 = randint(1, 9), randint(1,9)
            ans = int(input(f'{n1}*{n2} = '))
            o -= 1
            n = n1 * n2
            print(n)
        except ValueError:
            print('видите только целые числа!')
            continue
        if ans == n:
            file.write(f'{n1} * {n2} = {ans} ({n})- правильно!\n')
        else:
            file.write(f'{n1} * {n2} = {ans} ({n})-не правильно\n!')

    else:
        file.write(f'было попыток: {i}, потрачено времени: {datetime.now()-start_time}, имя: {player}\n\n')
