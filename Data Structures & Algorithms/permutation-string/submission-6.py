class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mapS1 = {}
        for char in s1:
            mapS1[char] = mapS1.get(char, 0) + 1
        print(mapS1)
        maxLen = len(s1)
        l = 0
        freq = {}
        for r in range(len(s2)):
            freq[s2[r]] = freq.get(s2[r], 0) + 1
            currLen = r - l + 1
            print(currLen)
            print(freq)
            if (l > len(s2) - 1):
                return False
            elif currLen == maxLen:
                if freq == mapS1:
                    return True
                # remove the element l is at and decrease its count
                if s2[l] in freq:
                    freq[s2[l]] = freq.get(s2[l], 1) - 1
                if freq.get(s2[l]) == 0:
                    del freq[s2[l]]
                l += 1
        return False
                

                
        