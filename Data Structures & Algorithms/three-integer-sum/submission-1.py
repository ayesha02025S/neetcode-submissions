class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result =[]
        nums.sort()

        for index, value in enumerate(nums):
            if index > 0 and value == nums[index-1]: # not first value in array and this value is equal to nums [i-1] that means its the same value as before 
                continue # we want to continue dont want to reuse the same value twice 
            left, right = index+1, len(nums) -1 
            while left < right:
                threeSum = value + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1 
                else:
                    result.append([value, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return result