class Solution:
    # approach 1
    # [1,2,2,3,3,3] -> [(1, 1), (2, 2), (3, 3)] (sorted) 
    # -> iterate from the back of the array from k = 2 to k = 0 and add to res
    # n -> buckets (each bucket is the frequency count of the number)
    # approach 2 
    # create a hash map to store frequency count for each number
    # where each key in the hashmap maps to its frequency count
    # create an array as the same size of the hash map 
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            hashMap[nums[i]] = hashMap.get(nums[i], 0) + 1
        
        buckets = [[] for i in range(len(nums) + 1)]

        for key, value in hashMap.items():
            buckets[value].append(key)
        
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res

            

        