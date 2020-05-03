x = int(input('Введите 1ое число: '))
y = int(input('Введите 2ое число: '))
z = int(input('Введите 3е число: '))

def summarize(x, y ,z):
    return x + y + z


print('Сумма трех чисел:',summarize(x, y, z))