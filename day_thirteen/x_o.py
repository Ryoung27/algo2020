def xo(s):
    possible_o = ['o', 'O', 0]
    possible_x = ['x', 'X']
    o = 0
    x = 0
    for i in s:
        if i in possible_o:
            o += 1
        if i in possible_x:
            x += 1
    if x == o:
        return True
    else:
        return False
