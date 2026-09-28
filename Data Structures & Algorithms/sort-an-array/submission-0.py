class Solution:
    def merge(self,low,mid,high,nums):
        l1=low
        l2=mid+1
        temp=[]
        while(l1<=mid and l2<=high):
            if nums[l1] <= nums[l2]:
                temp.append(nums[l1])
                l1+=1
            else:
                temp.append(nums[l2])
                l2+=1
        while (l1<=mid):
            temp.append(nums[l1])
            l1+=1
        while l2 <= high:
            temp.append(nums[l2])
            l2 += 1
            
        for i in range(len(temp)):
            nums[low + i] = temp[i]


    def mergeSort(self,low,high,nums):
        if low>=high:
            return
        mid=(low+high) // 2
        self.mergeSort(low,mid,nums)
        self.mergeSort(mid+1,high,nums)
        self.merge(low,mid,high,nums)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(0,len(nums)-1,nums)
        return nums