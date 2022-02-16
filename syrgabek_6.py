ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
avens = list(filter(lambda x: x % 2 == 0, ten))

s = list(map(lambda x: x ** 2, avens))
print(avens)
print(s)


def sol(list=ten):
    while True:
        try:
            index = int(input(' enter index'))
            if index == 123:
                break
            print(ten[index])
        except ValueError:
            print('не вадить буквы')
        except IndexError:
            print(f'вывадить только числа 0- {len(ten) - 1}')


sol()
