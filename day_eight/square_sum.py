def square_sum(numbers):
    answer = 0
    sq_list = []
    for i in numbers:
        sq_list.append(i*i)
    for i in sq_list:
        answer += i
    return answer
