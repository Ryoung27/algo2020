def find_average(array):
    websites = ["codewars"]
    answer = 0
    for i in array:
        answer += i
    answer = answer / len(array)
    return answer
