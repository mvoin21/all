year = int(input("Enter a year: "))

def years(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                b = "{0} is a leap year".format(year)
            else:
                b = "{0} is not a leap year".format(year)
                return b
        else:
            b = "{0} is a leap year".format(year)
            return b
    else:
        b = "{0} is not a leap year".format(year)
        return b

print(years(year))