def hackerrankInString(s):
    main = "hackerrank"
    result = 0
    for word in main:
        for d in range(1,len(s)+1):
            if word == s[d-1:d]:
                s = s[d:]
                result += 1
                break

    if result == 10:
        return "YES"
    else:
        return "NO"