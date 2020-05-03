m = input()
if m.count('f') < 2 and m.count('f') > 0:
    print(m.find('f'))
elif m.count('f') > 1:
    print(m.find('f'), m.rfind('f'))
else:
    print('')