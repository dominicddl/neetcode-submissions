class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = float('inf')

        for i in range(len(nums)):
            if nums[i] < minimum:
                minimum = nums[i]
        
        return minimum
        