class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1=len(s1)
        n2=len(s2)

        chars1=[0]*26
        chars2=[0]*26
        if n1>n2:
            return False
        
        for i in range (n1):
            chars1[ord(s1[i])-97]+=1
            chars2[ord(s2[i])-97]+=1

        if chars1==chars2:
            return True
        
        for i in range (n1,n2):
            chars2[ord(s2[i])-97]+=1
            chars2[ord(s2[i-n1])-97]-=1
            
            if chars2==chars1:
                return True
        return False

