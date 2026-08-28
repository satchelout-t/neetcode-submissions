class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        len(nums)
        num=set(nums)
        max_count=0
        for n in num:
            if n-1 not in num:
                count=1
                current=n
                while current+1 in num:
                    count+=1
                    current=current+1
                if count>max_count:
                    max_count=count
        return max_count