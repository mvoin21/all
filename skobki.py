def isBalanced(s):
    while '()' in s or '[]' in s or '{}' in s:
        s = s.replace('()', '')
        s = s.replace('[]', '')
        s = s.replace('{}', '')
    if s == '':
        return 'YES'
    return 'NO'