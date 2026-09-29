class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def combSum(idx,nums,target,temp,ans) :
            if idx>=len(nums) or target<0:
                if target==0:
                    ans.append(temp.copy())
                return
            temp.append(nums[idx])
            combSum(idx,nums,target-nums[idx],temp,ans)
            temp.pop()
            combSum(idx+1,nums,target,temp,ans)
        temp=[]
        ans=[]
        combSum(0,nums,target,temp,ans)
        return ans