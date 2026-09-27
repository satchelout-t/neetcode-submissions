class Solution:
    def seq(self,idx,temp,nums,ans):
        if idx > len(nums)-1:
            ans.append(temp.copy())
            return
        temp.append(nums[idx])
        self.seq(idx+1,temp,nums,ans)
        temp.pop()
        self.seq(idx+1,temp,nums,ans)
        
    def subsets(self, nums: list[int]) -> list[list[int]]:
        temp=[]
        ans=[]
        self.seq(0,temp,nums,ans)
        return ans