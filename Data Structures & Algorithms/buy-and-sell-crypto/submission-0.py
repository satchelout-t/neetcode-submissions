class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n=len(prices)
        cheapeset=prices[0]
        maxP=0
        for i in range(n):
            if prices[i]<cheapeset:
                cheapeset=prices[i]
            currp=prices[i]-cheapeset
            if maxP<currp:
                maxP=currp
        return maxP