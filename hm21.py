def long_(string):
    for item in string:
        if item in [',', '!', '.', '(', ')']:
           string = string.replace(item, ' ')
    list_ = string.split(' ')
    longer = max(list_, key=len)
    return longer


strng = str(input('Введите строку: '))
print('Cамаое длинное слово:', long_(strng))
