class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        R = 0
        for i in s:
            if i == 'R':
                count += 1
            else:
                count -= 1
            if count == 0:
                R += 1
        return R
