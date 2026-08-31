class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        max_left=[0]*n
        max_right=[0]*n
        leftwall=0
        rightwall=0
        for i in range (0,n):
            j=-i-1
            max_left[i]=leftwall
            max_right[j]=rightwall
            leftwall=max(leftwall,height[i])
            rightwall=max(rightwall,height[j])

        total_water=0
        for i in range (n):
            potential_water=min(max_left[i],max_right[i])
            actual=potential_water-height[i]
            if actual>0:
                total_water+=actual
        return total_water
  