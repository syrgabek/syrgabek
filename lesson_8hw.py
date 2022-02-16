import random
import datetime

player = input('введите имя')
o = int(input('количество попыток'))
i = o
start_time = datetime.datetime.now()
with open('resylst.txt', 'a', encoding='UTF-8')as  file:
    while o != 0:
        x = random.randint(1, 9)
        y = random.randint(1, 9)
        w = x * y
        try:
            answer = int(input(f'{x}*{y}= ?'))
            o -= 1
            if answer != w:
                f'Не праильный ответ.\n' \
                f'Осталась {o} попыток'
                file.write(f'{x}*{y}={answer}({w}) не правильно')
    else:
        print('правильный ответ\n'
                f'осталась попыток')
        file.write(f"{x} * {y} = {answer}({w})"\n
                   f'правильно\n')
        except ValueError:
            print('водите только числа datetime.datetime.now()-start_time')
        file.write(f"було{i}попыток,потраченное вреья'\
           f'{i},имя{player}\n")
print("спасибо за игру")