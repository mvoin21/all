list_numbers = input('Введите числа через запятую: ').split(',')
integer_nmbrs = list(map(int, list_numbers))
def get_minimal_positive():
    min_ = []
    for i in integer_nmbrs:
        if i + 1 not in integer_nmbrs and i >= 0:
            min_.append(i+1)
            return min(min_)
        elif i <= 0:
            if 1 not in integer_nmbrs:
                return '1'
            
print(f'Минимальное позитивное число: {minimal_positive()}')
