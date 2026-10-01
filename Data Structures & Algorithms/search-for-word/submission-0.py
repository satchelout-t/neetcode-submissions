class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m=len(board)
        n=len(board[0])
        w=len(word)
        if m==1 and n==1:
            return board[0][0]==word
        def solve(pair,idx):
            i,j=pair
            if idx==w:
                return True
            if board[i][j]!=word[idx]:
                return False
            
            char=board[i][j]
            board[i][j]='#'
            for i_off, j_off in [(0,1),(1,0),(-1,0),(0,-1)]:
                r=i+i_off
                c=j+j_off
                if 0<=r<m and 0<=c<n:
                    if solve((r,c),idx+1):
                        return True
            board[i][j]=char
            return False
                    
        for i in range(m):
            for j in range(n):
                if solve((i,j),0):
                    return True
        return False