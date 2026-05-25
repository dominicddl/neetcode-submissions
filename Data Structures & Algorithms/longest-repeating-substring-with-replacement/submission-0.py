class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # hash map to count freq
        count = {}
        res = 0 
        l = 0
        for r in range(len(s)):
            # get the count of the freq, if not default to 0
            count[s[r]] = 1 + count.get(s[r], 0)

            # check if window is valid
            
            while (r - l + 1) - max(count.values()) > k: 
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res



        