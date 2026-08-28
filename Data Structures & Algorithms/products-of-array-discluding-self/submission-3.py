class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result=[1]*n
        prefix=[1]*n
        for i in range (1,n):
            prefix[i]=prefix[i-1]*nums[i-1]
        sufix=1
        for i in range (n-1,-1,-1):
            result[i]=prefix[i]*sufix
            sufix=sufix*nums[i]
        return result 
