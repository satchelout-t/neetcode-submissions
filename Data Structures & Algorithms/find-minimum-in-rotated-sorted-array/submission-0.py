
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        l , r = 0 , n-1
        ans_min=float('inf')
        while(l<=r):
            mid = (l + r) // 2
            if nums[l] <= nums [mid] and nums[r]>nums [mid]:
                ans_min=min(nums[l],ans_min)
            if nums[l] <= nums [mid]:
                # left half is sorted 
                ans_min=min(nums[l],ans_min)
                l=mid+1
            else:
                #right half is sorted 
                ans_min=min(nums[mid],ans_min)
                r=mid-1
            
        return ans_min

