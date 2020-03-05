def to_jaden_case(string):
    answer = ''
    j_list = []
    j_cap = []
    j_list = string.split()
    for i in j_list:
        j_cap.append(i.capitalize())
    answer = ' '.join(j_cap)
    return answer
