class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rCount, cCount = [0] * m , [0] * n
        res = 0

        arr = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rCount[i] += 1
                    cCount[j] += 1
                    arr.append([i, j])

        for i, j in arr:
            if rCount[i] > 1 or cCount[j] > 1:
                res += 1
        return res