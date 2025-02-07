class Solution:
    LEN_BOARD = 9
    def solveSudoku(self, board: List[List[str]]) -> None:
        num_row_map = defaultdict(set)
        num_col_map = defaultdict(set)
        num_sub_square_map =defaultdict(set)
        def dfs(i, j):
            if i == self.LEN_BOARD:
                return True
            if board[i][j] != ".": return dfs(i, j + 1) if j + 1 < self.LEN_BOARD else dfs(i+1, 0)
            for k in '123456789':
                sub_square = self.get_sub_square_from_idx(i, j)
                if i in num_row_map[k] or j in num_col_map[k] or sub_square in num_sub_square_map[k]:
                    continue
                board[i][j]=k
                num_row_map[k].add(i)
                num_col_map[k].add(j)
                num_sub_square_map[k].add(sub_square)
                res = dfs(i, j + 1) if j + 1 < self.LEN_BOARD else dfs(i+1, 0)
                if res: return True
                board[i][j] = "."
                num_col_map[k].remove(j)
                num_row_map[k].remove(i)
                num_sub_square_map[k].remove(sub_square)
            return False

        for i in range(self.LEN_BOARD):
            for j in range(self.LEN_BOARD):
                num = board[i][j]
                if num != ".":
                    num_row_map[num].add(i)
                    num_col_map[num].add(j)
                    num_sub_square_map[num].add(self.get_sub_square_from_idx(i,j))
        dfs(0, 0)


    def get_sub_square_from_idx(self, i, j):
        return (i // 3) * 3 + j // 3
