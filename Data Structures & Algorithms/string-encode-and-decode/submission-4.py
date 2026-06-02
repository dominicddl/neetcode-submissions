import base64

class Solution:
    # loop through each string and 
    # demarcating character like '#'
    # then when decoding, the decoder checks for the start and end of the
    # '#' character, e.g. when an encoded byte starts with a '#', decode 
    # until the next '#', add that decoded word onto the list of strings
    def encode(self, strs: List[str]) -> str:
        res_encoded = ""
        for s in strs:
            res_encoded += str(len(s)) + "#" + s
        
        print(res_encoded)
        return res_encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            j += 1
            res.append(s[j:j + length])
            i = j + length
        
        return res