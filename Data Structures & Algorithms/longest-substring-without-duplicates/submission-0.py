class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = {}
        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] in sub:
                l = max(sub[s[r]] + 1, l)
            sub[s[r]] = r
            res = max(res, r - l + 1)
        return res


