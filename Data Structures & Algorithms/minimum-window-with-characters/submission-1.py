class Solution(object):
    def minWindow(self, s, t):
        n = len(s)
        m = len(t)
        if m > n or m == 0:
            return ""

        hashmap = [0] * 256
        for ch in t:
            hashmap[ord(ch)] += 1

        min_length = float('inf')
        str_id = 0
        cnt = 0
        l = 0
        r = 0

        while r<n:
            if hashmap[ord(s[r])]>0:
                cnt=cnt+1
            hashmap[ord(s[r])]-=1

            while (cnt==len(t)):
                length=r-l+1
                if length < min_length:
                    min_length=length
                    str_id=l
                hashmap[ord(s[l])] += 1
                if hashmap[ord(s[l])] > 0:
                    cnt -= 1
                l += 1
            r += 1
        if min_length == float('inf'):
            return ""
        ans = ""
        for i in range(str_id, str_id + min_length):
            ans = ans + s[i]
        return ans