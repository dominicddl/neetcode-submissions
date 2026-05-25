class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        if s == t: return s
        t1 = {}
        for char in t:
            t1[char] = t1.get(char, 0) + 1
        
        have, need  = 0, len(t1)
        freq = {}
        res = [-1, -1]
        resLen = float('inf')
        l = 0
        for r in range(len(s)):
            c = s[r]
            freq[c] = freq.get(c, 0) + 1
            if c in t1 and freq[c] == t1[c]:
                have += 1
            
            while have == need: 
                if (r - l + 1) < resLen:
                    res = [l ,r]
                    resLen = r - l + 1
                
                freq[s[l]] -= 1
                if s[l] in t1 and freq[s[l]] < t1[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r + 1] if resLen != float('inf') else ""
        