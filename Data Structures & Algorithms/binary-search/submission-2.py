class Solution:
    def recursive(self, l: int, h: int, nums: List[int], target: int) -> int:
        if l > h:
            return -1
        mid = l + (h - l) // 2
        if (nums[mid] == target):
            return mid
        elif nums[mid] < target:
            return self.recursive(mid + 1, h, nums, target)
        elif nums[mid] > target:
            return self.recursive(l, mid - 1, nums, target)
    def search(self, nums: List[int], target: int) -> int:
        return self.recursive(0, len(nums) - 1, nums, target)
