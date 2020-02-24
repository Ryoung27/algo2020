def sum_array(arr):
    #your code here
    answer = 0
    if arr == None or arr == []:
        return 0
    if len(arr) < 3:
        return 0
    arr.sort()
    arr = arr[1:-1:]
    for i in arr:
        answer += i
    return answer
