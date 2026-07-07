class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in board:
            seen = set()
            for char in i:
                if char == ".":
                    continue
                if char not in seen:
                    seen.add(char)
                else:
                    return False
                    
        for i in range(9):
            seen = set()
            for j in range(9):
                char = board[j][i]
                if char == ".":
                    continue
                if char not in seen:
                    seen.add(char)
                else:
                    return False
        
        for row_start in range(0,9,3):
            for col_start in range(0,9,3):

                seen = set()

                for i in range(3):
                    for j in range(3):
                        char = board[row_start+i][col_start+j]
                        if char == ".":
                            continue
                        if char not in seen:
                            seen.add(char)
                        else:
                            return False

        return True
