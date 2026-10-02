class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if digits=="":
            return []
        keypad={'2':'abc', '3':'def', '4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        
        n=len(digits)
        def solve(idx,sol):
            if idx==n:
                ans.append(''.join(sol))
                return
            for letter in keypad[digits[idx]]:
                sol.append(letter)
                solve(idx+1,sol)
                sol.pop()
        sol=[]
        ans=[]
        solve(0,sol)
        return ans


        