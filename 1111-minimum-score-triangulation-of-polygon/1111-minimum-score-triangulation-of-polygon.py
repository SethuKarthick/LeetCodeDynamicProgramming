from typing import List

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)

        # Initialize memo table with -1 to represent "not computed yet"
        memo = [[-1] * n for _ in range(n)]

        def dp(i, j):

            if memo[i][j] != -1:
                return memo[i][j]


            if j - i < 2:
                return 0  # No triangle can be formed

            min_score = float('inf')

            for k in range(i + 1, j):
                score = values[i] * values[k] * values[j]
                total = dp(i, k) + dp(k, j) + score
                min_score = min(min_score, total)

            memo[i][j] = min_score
            return min_score

        return dp(0, n - 1)
