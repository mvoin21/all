def palindrom(words):
    reverse = words[::-1]
    r = reverse.split(' ')
    reverse = ''.join(r)
    w = words.split(' ')
    words = ''.join(w)
    if words.lower() == reverse.lower():
        print(True)
    else:
        print(False)

text = str(input('Введите слово или строку: '))
palindrom(text)