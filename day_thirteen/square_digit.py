def square_digits(num):
    print(num)
    answer = ''
    num = str(num)
    for i in num:
        int_answer = int(i) * int(i)
        answer += str(int_answer)
    return int(answer)
