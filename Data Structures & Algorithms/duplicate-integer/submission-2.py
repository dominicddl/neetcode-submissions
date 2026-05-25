class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Create hash map for nums
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1
            if count.get(nums[i]) > 1:
                return True
        return False

        