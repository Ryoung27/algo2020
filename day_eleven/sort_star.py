def two_sort(array):
    answer = ''
    array.sort()
    print(array)
    for i in array[0]:
        answer += i + '***'
    answer = answer[:-3]
    return answer
    
