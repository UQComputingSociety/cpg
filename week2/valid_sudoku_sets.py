# By Kenton Lam

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # set up sets for ea
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for r, row in enumerate(board):
            for c, val in enumerate(row):
                if val == '.': continue
                row_set = rows[r]
                col_set = cols[c]
                box_set = boxes[3*(r//3) + c//3]
                for s in (row_set, col_set, box_set):
                    if val in s: return False
                    s.add(val)  
        return True