class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[l] == target:
                return l
                break
            elif nums[r] == target:
                return r
                break

            mid = l + ((r - l) // 2)
            if nums[mid] == target:
                return mid
                break

            if nums[l] <= nums[mid]:
                if nums[l] < target and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1 
            else:
                if nums[mid] < target and target < nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        # target not found
        return -1