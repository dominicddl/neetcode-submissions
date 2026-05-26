class Solution:
    # hash map that stores both the current integer, index of the integer
    # we iterate over the array, find the difference between the target and the current int
    # if this difference, is already a key in the hashmap, we get the value of this key and return 
    # the current index and the index of the existing key in the hashmap 
    # otherwise if the difference is not a key in the hashmap, then we store the current int and its index
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} 
        res = list()
        for idx, val in enumerate(nums):
            diff = target - val
            correct = diff in hashMap
            if diff in hashMap:
                res.append(hashMap[diff])
                res.append(idx)
            hashMap[val] = idx
        
        return res
        