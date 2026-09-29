class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        def combSum2(idx, nums, temp, target, ans):
            if target == 0:
                ans.append(temp.copy())
                return

            if idx == len(nums) or target < 0:
                return
            
            temp.append(nums[idx])
            combSum2(idx + 1, nums, temp, target - nums[idx], ans)
            temp.pop()
            index=idx+1
            while(index<len(nums) and nums[index]==nums[idx]):
                index+=1
            combSum2(index, nums, temp, target, ans)
        ans=[]
        temp=[]
        combSum2(0,candidates,temp,target,ans)
        return ans