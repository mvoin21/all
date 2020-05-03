def fahrenheit(x):
    celsius = (float(x) - 32) * 5/9
    return celsius

def celsius(x):
    fahrenheit = (float(x) * 9/5) + 32
    return fahrenheit


while True:
    finish = input('Нажмите enter или введите exit для завершения: ')
    if finish.lower() == 'exit':
        print('Программа завершина.\nFrom Makers with LOVE;)')
        break
    else:
        print('Выберите вариант действия:')
        print('1) Celsius => Fahrenheit')
        print('2) Fahrenheit => Celsius')
        m = (input())
        if int(m) > 2 or int(m) <= 0:
            print('Некорректный ввод')
            continue
        elif int(m) == 1:
            g = input('Введите число: ')
            print(celsius(g), 'F', sep='')
        elif int(m) == 2:
            f = input('Введите число: ')
            print(fahrenheit(f), 'C', sep='')
    