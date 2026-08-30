class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        triplet=set()
        ans=[]
        for i in range (n):
            k_values={}
            for j in range (i+1,n):
                sum_ij=nums[i]+nums[j]
                if (-sum_ij) in k_values:
                    new_triplet=[nums[i],nums[j],-sum_ij]
                    new_triplet=sorted(new_triplet)
                    triplet.add(tuple(new_triplet))
                k_values[nums[j]]=1
        for numbers in triplet:
            ans.append(numbers)
        return ans