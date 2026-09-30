class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def solve(idx,nums,temp,ans):
            if idx==len(nums):
                ans.append(temp.copy())
                return
            temp.append(nums[idx])
            solve(idx+1,nums,temp,ans)
            temp.pop()
            newidx=idx+1
            while(newidx<len(nums) and nums[newidx]==nums[idx]):
                newidx+=1
            solve(newidx,nums,temp,ans)
        ans=[]
        nums = sorted(nums)
        solve(0,nums,[],ans)
        return ans