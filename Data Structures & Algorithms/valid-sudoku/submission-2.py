class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_dict = defaultdict(set)
        cols_dict = defaultdict(set)
        quad_dict = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                if val in rows_dict[r] or val in cols_dict[c] or val in quad_dict[(r//3, c//3)]:
                    return False
                rows_dict[r].add(val)
                cols_dict[c].add(val)
                quad_dict[(r//3, c//3)].add(val)

        return True