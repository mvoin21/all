def sorti(x):
    x = x.split()
    x.sort(key=len)
    result = " ".join(x)
    print(result)

text = str(input('Введите текст через пробел: '))   
sorti(text)
