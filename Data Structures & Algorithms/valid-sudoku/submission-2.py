class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] in seen and board[row][i] != ".":
                    return False
                seen.add(board[row][i])
        
        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] in seen and board[i][col] != ".":
                    return False
                seen.add(board[i][col])
        
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] in seen and board[row][col] != ".":
                        return False
                    seen.add(board[row][col])

        return True

        board=[ [".",".","4",".",".",".","6","3","."],
                [".",".",".",".",".",".",".",".","."],
                ["5",".",".",".",".",".",".","9","."],
                [".",".",".","5","6",".",".",".","."],
                ["4",".","3",".",".",".",".",".","1"],
                [".",".",".","7",".",".",".",".","."],
                [".",".",".","5",".",".",".",".","."],
                [".",".",".",".",".",".",".",".","."],
                [".",".",".",".",".",".",".",".","."]]