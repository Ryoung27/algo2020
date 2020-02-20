class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        for i in A:
            count = A.count(i)
            if count > 1:
                return i
            else:
                pass
        
