class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])
        result = [[0 for _ in range(row)] for _ in range(col)]

        for n in range(col):
            for m in range(row):
                result[n][m] = matrix[m][n]

        return result 