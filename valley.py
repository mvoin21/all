def countingValleys(n, s):
    mounts = 0
    valleys = 0
    if n >= 2 and n <= 10**6:
        for i in s:
            if i == 'U' or 'D':
                for i in range(n):
                    if s[i] == 'U':
                        mounts += 1
                        if mounts == 0:
                            valleys += 1
                    else:
                        mounts -= 1
                return valleys