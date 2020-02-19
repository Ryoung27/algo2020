class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        answer = []
        for i in A:
            answer.append(i * i)
        answer.sort()
        return answer
