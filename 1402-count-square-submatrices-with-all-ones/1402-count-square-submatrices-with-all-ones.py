class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        row = len(matrix)
        col = len(matrix[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]

        total = 0

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])


                total += dp[i][j]

        return total

