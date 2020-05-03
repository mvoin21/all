print('Hello, which office do you need?')
office = input("""
1) Google Kazakstan
2) Google Paris
3) Google Uar
4) Google Kyrgystan
5) Google San Francisco
6) Google Germany
7) Google Moscow
8) Google Sweden
Enter number: """)
    
if int(office) == 1:
    text = input('Please write your wishes or complaint:\n')
    with open('google_kazakstan', mode='w') as f:
        f.write(text)
        f.close()
elif int(office) == 2:
    text = input('Please write your wishes or complaint:\n')
    with open('google_paris', mode='w') as f:
        f.write(text)
        f.close()
elif int(office) == 3:
    text = input('Please write your wishes or complaint:\n')
    with open('google_uar', mode='w') as f:
        f.write(text)
        f.close()
elif int(office) == 4:
    text = input('Please write your wishes or complaint:\n')
    with open('google_kyrgystan', mode='w') as f:
        f.write(text)
        f.close()
elif int(office) == 5:
    text = input('Please write your wishes or complaint:\n')
    with open('google_san_francisco', mode='w') as f:
        f.write(text)
        f.close()
elif int(office) == 6:
    text = input('Please write your wishes or complaint:\n')
    with open('google_germany', mode='w') as f:
        f.write(text)
        f.close()
elif int(office) == 7:
    text = input('Please write your wishes or complaint:\n')
    with open('google_moscow', mode='w') as f:
        f.write(text)
        f.close()
elif int(office) == 8:
    text = input('Please write your wishes or complaint:\n')
    with open('google_sweden', mode='w') as f:
        f.write(text)
        f.close()


