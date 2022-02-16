import random

count = 0
number = random.randint(1, 100)

while True:
    count += 1

    print(number)
    enter = int(input("Введите число : "))

    if number == enter:
        print('Вы угадали\nТак просто... Всего ' + str(count) + ' попыток :))))\n\n' + str(number))


    elif enter <= number + 5 and enter >= number - 5:
        if enter < number:
            print("очень близко, пиши больше\n")
        else:
            print("очень близко, пиши меньше\n")

    elif enter <= number + 10 and enter >= number - 10:
        if enter < number:
            print("близко, пиши больше\n")
        else:
            print("близко, пиши меньше\n")
    elif enter <= number + 99 and enter >= number - 99:
        if enter < number:
            print("пиши больше")
        else:
            print("пиши меньше")


