class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # define our hash set 
        numSet = set()

        for num in nums:
            if num in numSet:
                return True
            numSet.add(num)
        
        # if no duplicates
        return False
        