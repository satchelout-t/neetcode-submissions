class Solution:
    def partition(self, s: str) -> list[list[str]]:
        def palindrome(piece):
            l = 0
            r = len(piece) - 1
            while l < r:
                if piece[l] != piece[r]:
                    return False
                l = l + 1
                r = r - 1
            return True

        def solve(temp,rest,ans):
            if len(rest)==0:
                ans.append(temp.copy())
                return
            for i in range (0,len(rest)):
                piece=rest[0:i+1]
                if palindrome(piece):
                    temp.append(piece)
                    solve(temp,rest[i+1:len(rest)],ans)
                    temp.pop()
        ans = []
        solve([],s,ans)
        return ans
