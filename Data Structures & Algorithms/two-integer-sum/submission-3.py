class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        sum = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            sum[diff] = sum.get(diff, i)
            if nums[i] in sum:
                res = [sum.get(nums[i]), i]
        
        return res
        