def abbrevName(name):
    answer = ''
    name = name.split(' ')
    for i in name:
        answer += i[0]
    answer = answer[:1] + '.' + answer[1:]
    answer = answer.upper()
    return answer
