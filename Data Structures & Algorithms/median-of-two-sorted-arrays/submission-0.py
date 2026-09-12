class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m=len(nums1)
        n=len(nums2)
        sorted_nums=[0]*(n+m)
        i,j = 0,0 
        k=0
        while (i<m and j<n): 
            if nums1[i] <= nums2[j]:
                sorted_nums[k]=nums1[i]
                i+=1
            else:
                sorted_nums[k]=nums2[j]
                
                j+=1
            k+=1
        while (i<m):
                sorted_nums[k]=nums1[i]
                k+=1
                i+=1
        while (j<n):
                sorted_nums[k]=nums2[j]
                k+=1
                j+=1 
        idx=(n+m) // 2
        if (n+m) % 2 == 1:
            return float(sorted_nums[idx]) 
        else:
            return (sorted_nums[idx] + sorted_nums[idx-1]) / 2.00