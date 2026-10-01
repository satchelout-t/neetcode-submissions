class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def solve(idx,cnt_o,cnt_c,temp,ans):
            if idx==2*n:
                ans.append(temp)
                return
            if cnt_o<n:
                temp = temp + "("
                solve(idx+1,cnt_o+1,cnt_c,temp,ans)
                temp = temp[:-1] 
            if cnt_o>cnt_c:
                temp=temp + ")"
                solve(idx+1,cnt_o,cnt_c+1,temp,ans)
                temp = temp[:-1]
        ans=[]
        solve(0,0,0,"",ans)
        return ans