def digitize(n):
    l = []
    answer = []
    n = str(n)
    for i in n:
        i = int(i)
        l.append(i)
    return l[::-1]
