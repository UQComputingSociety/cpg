class Solution:
    def getColumn(self, m: List[List[str]], i: int):
        return [row[i] for row in m]
    
    def checkIfUnique(self, l: List[str]) -> bool:
        l = list(filter(lambda x: x !=".", l))
        return len(l) - len(set(l)) == 0
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.isRowValid(board) \
           and self.isColumnValid(board) \
           and self.isSubValid(board)
    
    # Check every row
    def isRowValid(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            if not self.checkIfUnique(board[i]):
                return False
        return True
    
    # Get column from matrix, and check each one
    def isColumnValid(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            if not self.checkIfUnique(self.getColumn(board, i)):
                return False
        return True
    
    # Get sub-boxes from each one, and check each sub-box
    # (oh my this is slow)
    def isSubValid(self, board: List[List[str]]) -> bool:
        sub_boxes = []
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                sub_box = []
                for k in range(3):
                    for l in range(3):
                        sub_box.append(board[i + k][j + l])
                sub_boxes.append(sub_box)
        for box in sub_boxes:
            if not self.checkIfUnique(box):
                return False
        return True
