def accum(s):
    s = s.lower()
    answer = ""
    count = 0
    for i in s:
        count += 1
        new_addition = i * count + '-'
        new_addition = new_addition.capitalize()
        answer += new_addition
    answer = answer[:-1:]
    return answer
