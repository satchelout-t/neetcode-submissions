from math import ceil
class Solution:
    def validK(self,piles: List[int], k: int, h: int)-> bool:  
        if k == 0:
            return False
        taken_time = 0
        for bns in piles:
            taken_time += ceil(bns / k)   
        return taken_time <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n=len(piles)
        piles=sorted(piles)
        max_el=piles[n-1]
        l=0
        r=max_el
        min_k=float('inf')
        while(l<=r):
            mid = l + (r - l) // 2
            if self.validK(piles,mid,h):
                if min_k>=mid:
                    min_k=mid
                r=mid-1
            else:
                l=mid+1       
        return min_k