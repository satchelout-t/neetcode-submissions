class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        max_length=0
        mpp={}
        l,r=0,0
        while r < n:
            if s[r] in mpp and mpp[s[r]] >= l:  
                l = mpp[s[r]] + 1
            mpp[s[r]] = r                         
            length = r - l + 1                  
            if length > max_length:
                max_length = length
            r += 1
        return max_length