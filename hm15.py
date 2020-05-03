def time_walk(h, m, s):
    total = (h*60) + (m*60) + s
    return total

h = int(input('Enter hours: '))
m = int(input('Enter minutes: '))
s = int(input('Enter minutes: '))

h2 = int(input('Enter hours 2nd: '))
m2 = int(input('Enter minutes 2nd: '))
s2 = int(input('Enter minutes 2nd: '))

diference = time_walk(h, m, s) - time_walk(h2, m2, s2)

print(abs(diference))