def find_short(s):
    s = s.split(' ')
    return len(min((i for i in s), key=len))
