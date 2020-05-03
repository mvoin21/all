nmbrs = input('Введите числа через запятую: ')

def sort(numbers):
    list_num = numbers.split(',')
    positive = []
    negative = []
    for item in list_num:
        if int(item) > 0:
            positive.append(item)
        else:
            negative.append(item)
    print('Положительные числа:', positive)
    print('Отрицательные числа:', negative)

sort(nmbrs) 

