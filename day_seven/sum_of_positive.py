def positive_sum(arr):
    # Your code here
    answer = 0
    for i in arr:
        if i > 0:
            answer += i
    return answer


def positive_sum(arr):
    # Your code here
    answer = 0
    for i in arr:
        if i > 0:
#882 ms             answer += i
#823 ms            answer = answer + i
            answer = answer + i
    return answer
