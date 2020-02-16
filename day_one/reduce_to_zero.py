# My answer
class Solution:
    def numberOfSteps (self, num: int) -> int:
        count = 0
        while num != 0:
            if num % 2 == 0:
                num = num / 2
                count = count + 1
            else:
                num = num - 1
                count = count + 1
        return count

# Cleanest answer
class Solution:
    def numberOfSteps (self, num: int) -> int:
        digits = f'{num:b}'
        return digits.count('1') - 1 + len(digits)
