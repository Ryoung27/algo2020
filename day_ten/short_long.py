def solution(a, b):
    answer = ''
    if len(a) > len(b):
        answer = b + a + b
    else:
        answer = a + b + a
    return answer
