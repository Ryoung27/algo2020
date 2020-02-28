868ms
def high_and_low(numbers):
    # ...
    answer = ''
    numb_list = []
    print(numbers)
    numbers = numbers.split(' ')
    for i in numbers:
        numb_list.append(int(i))
    print(numb_list)
    numb_list.sort()
    print(numb_list)
#     print(numbers)
#     numbers.sort()
#     print(numbers)
    answer += str(numb_list[-1]) + ' ' + str(numb_list[0])
    return answer

def high_and_low(numbers):
    # ...
    answer = ''
    numb_list = []
    numbers = numbers.split(' ')
    for i in numbers:
        numb_list.append(int(i))
    numb_list.sort()
    answer += str(numb_list[-1]) + ' ' + str(numb_list[0])
    return answer
