class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        l = 0
        res = 0

        for r, c in enumerate(s):
            if c in last and last[c] >= l:
                l = last[c] + 1
            last[c] = r
            res = max(res, r - l + 1)

        return res