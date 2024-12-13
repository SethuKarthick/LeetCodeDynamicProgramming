class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subGrids = [set() for _ in range(9)]


        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != ".":
                    subGridLocation = (i // 3) * 3 + (j//3)


                    if element in rows[i] or element in cols[j] or element in subGrids[subGridLocation]:
                        return False

                    rows[i].add(element)
                    cols[j].add(element)
                    subGrids[subGridLocation].add(element)

        return True