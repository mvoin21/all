lst = input('Введите элементы через запятую: ')
lst = lst.split(',')
element = input('Введите искомый элемент: ')

def analysis(x, y):
    cnt = x.count(y)
    return cnt
        
cnt = analysis(lst, element)
print(f'{element}: {cnt}')
