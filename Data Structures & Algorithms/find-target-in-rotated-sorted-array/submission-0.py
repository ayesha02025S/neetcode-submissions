class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if target == nums[middle]:
                return middle

            # left sorted portion
            if nums[left] <= nums[middle]:
                if target > nums[middle] or target < nums[left]: # or target is too small then look on the right 
                    left = middle + 1
                else:
                    right = middle - 1
            # right sorted postion
            else:
                if target < nums[middle] or target > nums[right]:
                    right = middle - 1
                else:
                    left = middle + 1
        return -1






        