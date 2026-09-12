class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m=len(nums1)
        n=len(nums2)
        i,j = 0,0 
        k=0
        k1=(n+m) // 2
        k2=(n+m) // 2 - 1
        cnt=0
        k1_value=-1
        k2_value=-1
        while (i<m and j<n):  
            if nums1[i] <= nums2[j]:
                if cnt==k1 : k1_value=nums1[i]
                if cnt==k2 : k2_value=nums1[i]   
                i+=1
            else:
                if cnt==k1 : k1_value=nums2[j]
                if cnt==k2 : k2_value=nums2[j]   
                j+=1    
            cnt+=1   
        while (i<m):
                if cnt==k1 : k1_value=nums1[i]
                if cnt==k2 : k2_value=nums1[i]   
                i+=1
                cnt+=1   
        while (j<n):
                if cnt==k1 : k1_value=nums2[j]
                if cnt==k2 : k2_value=nums2[j]
                j+=1
                cnt+=1   
        if (n+m) % 2 == 1:
            return k1_value
        return (k1_value+k2_value) / 2.00