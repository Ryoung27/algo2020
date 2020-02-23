def find_average(nums):
    #your code here
    answer = 0
    for i in nums:
        answer += i
    if len(nums) > 0:
        answer = answer/ len(nums)
    else:
        answer = []
    return answer
