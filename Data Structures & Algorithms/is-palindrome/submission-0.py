class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        r=len(s)-1
        while (i<=r):
            while i <= r and not s[i].isalnum():
                i += 1
            while i <= r and not s[r].isalnum():
                r -= 1
            if i <= r:
                if s[i].lower() != s[r].lower():
                    return False
                i += 1
                r -= 1
        return True   