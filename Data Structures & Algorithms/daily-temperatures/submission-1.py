class Solution:
  def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stk = []
        n = len(temperatures)
        ans = [0] * n
        for i in range(n):
            while stk:
                temp, idx = stk[-1]
                if temperatures[i] > temp:
                    ans[idx] = i - idx
                    stk.pop()
                else:
                    break
            stk.append((temperatures[i], i))
        return ans