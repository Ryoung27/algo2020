class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        answer = []
        for i in A:
            if i % 2 == 0:
                answer.append(i)
        for x in A:
            if x % 2 != 0:
                answer.append(x)
        return answer
