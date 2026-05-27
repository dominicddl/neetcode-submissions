class Solution:
    # ["car", "rat", "arc"] -> [["rat"], ["arc", "car"]]
    # ["car"] = [["car"]]
    # [""] = [[""]]
    # all lowercase english letters
    # for each word create an array of size 26 each representing the letters from a - z, with their integer coutn
    # "car" -> [1, 0, 1, ... , 1, 0, 0, ...] (key)
    # key = [1, 0, 1, ... , 1, 0, 0, ...], value = "car" 
    # if the key is in the hashmap -> we get the value and store it in the list with the other anagrams
    # value for each key -> List[str]
    # we just get all the values in our hashMap and convert it to a list
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}

        for word in strs:
            # initiaise the array of size 26 
            letter_count = [0] * 26
            for char in word:
                # for each character in the word
                idx = ord(char) - ord('a')
                # update its counter in the array
                letter_count[idx] += 1
            # check if the array (key) is in the hash map
            # if inside, append word to the list 
            # else, instantiate a new list as the value and add the word to that list
            key = tuple(letter_count)
            if key not in hashMap:
                hashMap[key] = []
            hashMap[key].append(word)

        # convert all values in the hashMap into a list -> List[List[str]]
        res = list(hashMap.values())
        return res