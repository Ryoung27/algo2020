class Solution:
    def defangIPaddr(self, address: str) -> str:
        answer = ''
        for i in address:
            if i == '.':
                i = '[.]'
            answer = answer + i
        return answer
