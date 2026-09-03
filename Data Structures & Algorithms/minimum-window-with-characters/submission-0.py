class Solution(object):
    def minWindow(self, s, t):
        if t == "" or len(t) > len(s):
            return ""

        # 1. build what we NEED (count of each char in t)
        need_count = {}
        for c in t:
            if c in need_count:
                need_count[c] = need_count[c] + 1
            else:
                need_count[c] = 1

        need = len(need_count)      # number of DISTINCT chars we must satisfy
        have = 0                    # how many distinct chars are currently satisfied

        window = {}                 # counts of chars in the current window
        left = 0

        best_len = float('inf')     # length of best window so far (start "infinite")
        best_left = 0               # left index of best window

        # 2. expand the window with the right pointer
        for right in range(len(s)):
            c = s[right]

            # add c to the window
            if c in window:
                window[c] = window[c] + 1
            else:
                window[c] = 1

            # did c just reach exactly the amount t needs? then one more char satisfied
            if c in need_count and window[c] == need_count[c]:
                have = have + 1

            # 3. while the window is VALID, try to shrink from the left
            while have == need:
                # record this window if it's the smallest so far
                current_len = right - left + 1
                if current_len < best_len:
                    best_len = current_len
                    best_left = left

                # now remove the leftmost char to try to shrink
                left_char = s[left]

                # if it's about to drop BELOW the needed amount, we lose a satisfied char
                if left_char in need_count and window[left_char] == need_count[left_char]:
                    have = have - 1

                window[left_char] = window[left_char] - 1
                left = left + 1

        # 4. build the answer from the best window we recorded
        if best_len == float('inf'):
            return ""                       # never found a valid window
        return s[best_left : best_left + best_len]