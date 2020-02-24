def reverse_seq(n):
    answer = []
    list_range = range(1, n+1)
    for i in list_range:
        answer.append(i)
    answer.reverse()
    return answer
