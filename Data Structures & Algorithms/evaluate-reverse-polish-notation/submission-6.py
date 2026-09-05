from math import ceil,floor
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in ['+', '-', '*', '/']:
                a, b = stack.pop(), stack.pop()
                if t == '+':
                    res = b + a
                elif t == '-':
                    res = b - a
                elif t == '*':
                    res = b * a
                else: 
                    division = float(b) / a
                    if division >= 0:
                        res = floor(division)
                    else:
                        res = ceil(division)
                    res = int(res)
                stack.append(res)
            else:
                stack.append(int(t))
        return stack[0]