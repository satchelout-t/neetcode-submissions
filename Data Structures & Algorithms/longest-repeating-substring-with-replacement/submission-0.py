class Solution(object):
    def characterReplacement(self, s, k):
        n = len(s)
        count = {}
        l = 0
        max_length = 0
        for r in range(n):
            # add the new character entering on the right
            if s[r] in count:
                count[s[r]] = count[s[r]] + 1
            else:
                count[s[r]] = 1

            # find the most frequent character's count in the current window
            most_freq = 0
            for char in count:
                if count[char] > most_freq:
                    most_freq = count[char]

            # window length, and how many replacements it would need
            window_len = r - l + 1
            replacements_needed = window_len - most_freq

            # if it needs more than k replacements, shrink from the left
            while replacements_needed > k:
                count[s[l]] = count[s[l]] - 1
                l = l + 1
                window_len = r - l + 1
                replacements_needed = window_len - most_freq

            # record the best window seen
            if window_len > max_length:
                max_length = window_len

        return max_length