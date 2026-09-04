class Solution:
    def isValid(self, s: str) -> bool:
        n=len(s)
        match={')':'(','}':'{',']':'['}
        stack=[]
        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)
            else:
                if len(stack)==0:
                    return False
                if stack[-1] != match[ch]:
                    return False
                stack.pop()
        return len(stack) == 0
