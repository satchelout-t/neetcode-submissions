class Solution:
    def checkValidString(self, s: str) -> bool:
        min=0
        max=0
        for ch in s:
            if ch=="(":
                min+=1
                max+=1
            elif ch==")":
                min-=1
                max-=1
            elif ch=="*":
                min-=1
                max+=1
            if min<0:
                min=0
            if max<0:
                return False
        return min==0