class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m = len(grid)
        n = len(grid[0])

        maxFish = 0

        def dfs(row, col):
            fish = 0

            if grid[row][col] == 0:
                return fish 
            
            fish += grid[row][col]
            grid[row][col] = -1

            for r, c in directions:
                nRow, nCol = row + r , col + c
                if 0 <= nRow < m and 0 <= nCol < n:
                    if grid[nRow][nCol] > 0:
                        fish += dfs(nRow, nCol)

            return fish

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:
                    continue
                maxFish = max(maxFish, dfs(row, col))

        return maxFish
# class Solution:
#     def findMaxFish(self, grid: List[List[int]]) -> int:
#         directions = [[0,1], [0,-1], [1,0], [-1,0]]
#         m = len(grid)
#         n = len(grid[0])
#         maxFish = 0

#         def dfs(i: int, j: int, m: int, n: int) -> int:
#             fish = 0
            
#             if grid[i][j] == 0:
#                 return fish
            
#             fish += grid[i][j]
#             grid[i][j] = -1  # Visited

#             for dir in directions:
#                 nr = i + dir[0]
#                 nc = j + dir[1]
#                 if 0 <= nr < m and 0 <= nc < n:
#                     if grid[nr][nc] > 0:
#                         fish += dfs(nr, nc, m, n)
            
#             return fish

#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == 0:
#                     continue
#                 maxFish = max(maxFish, dfs(i, j, m, n))

#         return maxFish
        