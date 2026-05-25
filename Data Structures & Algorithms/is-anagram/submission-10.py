class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # initialising the hash maps
        sMap = {}
        tMap = {}

        # loop over both s and t to update the respective hash maps
        for c in s:
            sMap[c] = sMap.get(c, 1) + 1 
        
        for c in t:
            tMap[c] = tMap.get(c, 1) + 1
        
        # check whether the two hash maps are equal
        # equal -> same letters, same letter count
        return sMap == tMap
        