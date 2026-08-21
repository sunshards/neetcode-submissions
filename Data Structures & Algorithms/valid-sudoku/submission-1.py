class Solution:

    def hasDuplicates(self, nums: List[int]) -> bool:
        freqs = [0] * (len(nums)+1)
        for n in nums:
            if n == ".":
                continue
            n = int(n)
            if freqs[n] != 0:
                return True
            freqs[n]+=1
        return False

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowsLen = len(board)
        colsLen = len(board[0])
        cols = []

        for i in range(colsLen):
            c = []
            for j in range(rowsLen):
                c.append(board[j][i])
            cols.append(c)
        
        squares = []
        for i in range(9):
            square = []
            startRow = (i*3)%9
            startCol = (i//3)*3
            for j in range(3):
                for k in range(3):
                    square.append(board[startRow+j][startCol+k])
            squares.append(square)
        print(squares, sep="\n")
        
        combinations = board + cols + squares

        for c in combinations:
            if self.hasDuplicates(c):
                return False
        return True
        
