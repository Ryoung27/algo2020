# My Answer
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum_numb = 0
        n = str(n)
        for i in n:
            i = int(i)
            product = product * i
        for i in n:
            i = int(i)
            sum_numb = sum_numb + i
        return product - sum_numb
# Best Answer
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s, p = 0, 1
        for i in str(n): s += int(i); p *= int(i)
        return p - s
