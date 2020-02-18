class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in grid:
            for s in i:
                if s < 0:
                    count += 1
        return count
