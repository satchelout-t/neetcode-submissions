class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=[]
        nums=sorted(nums)
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            k=nums[i] 
            l=i+1
            r=n-1
            while (l<r):
                sum=nums[l]+nums[r]+k
                if sum==0:
                    ans.append([nums[l],nums[r],k])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:   
                        l += 1
                    while l < r and nums[r] == nums[r+1]: 
                        r -= 1
                elif sum>0:
                    r-=1
                else:
                    l+=1
        return ans
                