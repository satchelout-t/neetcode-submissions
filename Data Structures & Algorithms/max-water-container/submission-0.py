class Solution:
    def maxArea(self, nums: List[int]) -> int:
        n=len(nums)
        l=0
        r=n-1
        maxW=0
        while(l<r):
            length=r-l
            height=min(nums[l],nums[r])
            area=length*height
            if area>maxW:
                maxW=area
            if nums[l]>nums[r]:
                r-=1
            else:
                    l+=1
        return maxW  