from math import ceil,floor
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        n=len(tokens)
        for t in tokens:
            if t in '+-/*':
                res=''
                a,b =stack.pop(),stack.pop()
                if t=='+':
                    res=(b+a)
                elif t=='-':
                    res=(b-a)
                elif t=='*':
                     res=(b*a)
                else:
                    if (b/a) >= 0:
                        res=floor(b/a)
                    if (b/a) < 0:
                        res=ceil(b/a) 
                stack.append(res)
            else:
                stack.append(int(t))
        return stack[0]