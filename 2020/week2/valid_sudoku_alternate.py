# By Rowan Evans

class Solution:
    def validate(self,lines):
        for line in lines:
            line = list(filter(lambda x: x!=".",line))
            if len(line) != len(set(line)):
                return False
        return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not self.validate(board):
            return False
        transformed = [[line[x] for line in board] for x in range(9)]
        if not self.validate(transformed):
            return False
        boxed = []
        for x in range(0,9,3):
            for y in range(0,9,3):
                box = []
                for z in range(x,x+3):
                    box += board[z][y:y+3]
                boxed.append(box)
        if not self.validate(boxed):
            return False
        print(boxed)
        return True