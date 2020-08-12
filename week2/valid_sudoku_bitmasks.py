# By Kenton Lam

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # set up bit masks for each row/col/box.
        rows = 0
        cols = 0
        boxes = 0
        N = 9
        for r, row in enumerate(board):
            for c, val in enumerate(row):
                if val == '.': continue
                val = int(val)
                b = 3*(r//3) + c//3
                # c s s e 2 0 1 0
                existing = (
                    (rows >> (r*N + val))
                    | (cols >> (c*N + val))
                    | (boxes >> (b*N + val))
                )
                if existing & 1:
                    return False
                rows |= 1 << (r*N + val)
                cols |= 1 << (c*N + val)
                boxes |= 1 << (b*N + val)
        return True