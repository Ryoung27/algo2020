def sum_array(a):
    value = 0
    answer = 0
    if a == []:
        answer = 0
    else:
        for i in a:
            value += i
        answer = value
    return answer
