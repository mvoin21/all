def onTheMoon(weight: float) -> float:
    list_ = []
    for year in range(1, 16):
        weight += 1
        result = round(weight * 0.165, 2)
        list_.append(result)
    for num, wght in enumerate(list_, 1):
        print(f'{num} year: {wght}kg')


while True:
    finish = input('Нажмите enter или введите exit для завершения: ')
    if finish.lower() == 'exit':
        print('Программа завершина.')
        break
    try:
        weight = float(input('Введите Ваш вес: '))
    except Exception as e:
        print('Некорректный ввод!')
        continue
    onTheMoon(weight)
