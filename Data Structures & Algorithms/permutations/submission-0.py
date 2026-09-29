class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def solve(temp,mapp,ans,nums):
            if len(temp)==len(nums):
                ans.append(temp.copy())
                return
            for i in range(len(nums)):
                if mapp[i]==0:
                    mapp[i]=1
                    temp.append(nums[i])
                    solve(temp,mapp,ans,nums)
                    temp.pop()
                    mapp[i]=0
        ans=[]
        mapp=[0]*len(nums)
        temp=[]
        solve(temp,mapp,ans,nums)
        return ans