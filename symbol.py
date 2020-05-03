def smbl():
    text = input('Введите текст: ')
    if ', ' in text:
        text = text.replace(', ', ' ')

    if ' (' or '(' in text:
        text = text.replace(' (', ' ')

    if ') ' or ')' in text:
        text = text.replace(') ', ' ')
    if '. ' or '.' in text:
        text = text.replace('. ', ' ')
    
    if '! ' or '!' in text:
        text = text. replace('! ', ' ')

    text_ = text.split(' ')
    text = ' '.join(text_)
    print(text)

smbl()