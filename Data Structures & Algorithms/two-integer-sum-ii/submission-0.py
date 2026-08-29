class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        i=0
        r=n-1
        while (i<r):
            if (numbers[i]+numbers[r]==target):
                return [i+1,r+1]
            elif (numbers[i]+numbers[r]>target):
                r-=1
            else:
                i+=1
                 