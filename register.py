def sort(text):
    text = list(text)
    len_text = []
    lower_r = []
    upper_r = []
    for item in text:
        if item in [',', '.', '!', ':', ' ', '(', ')', '"']:
            continue
        else:
            len_text.append(item)

    for item in len_text:
        if item.isupper():
            upper_r.append(item)
        else:
            lower_r.append(item)
    high_precent = len(upper_r) / len(len_text) * 100
    lower_precent = len(lower_r) / len(len_text) * 100
    
    print(f'Букв в верхнем регистре: {round(high_precent, 2)}%')
    print(f'Букв в нижнем регистре: {round(lower_precent, 2)}%') 
    

text = str(input('Пожалуйста, введите Ваш текст: '))
sort(text)
