class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # for row
        for i in range(9):
            s=set()
            for j in range(9):
                item=board[i][j]
                if item in s:
                    return False
                elif item !=  '.':
                    s.add(item)
        for i in range(9):
            s=set()
            for j in range(9):
                item=board[j][i]
                if item in s:
                    return False
                elif item !=  '.':
                    s.add(item)
        
        for start_i in range(0, 9, 3):      # gives 0, 3, 6
            for start_j in range(0, 9, 3):  # gives 0, 3, 6
                s = set()
                for i in range(start_i, start_i + 3):
                    for j in range(start_j, start_j + 3):
                        item = board[i][j]
                        if item in s:
                            return False
                        elif item != '.':
                            s.add(item)
        return True
