class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxLen=0
        for i in range(len(nums)):
            if i>maxLen:
                return False
            currRlen=i+nums[i]
            if currRlen>maxLen:
                maxLen=currRlen
        return True 