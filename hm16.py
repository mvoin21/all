list_numbers = input('Введите числа через запятую: ')
list_numbers = list_numbers.split(',')


def num(*args):
    ends = []
    for item in list_numbers:
        if int(item) > 0:
            item = '1'
            ends.append(item)
        elif int(item) < 0:
            item = '-1'
            ends.append(item)
        else:
            ends.append(item)
    return ends

lists = num(list_numbers)
print(lists) 