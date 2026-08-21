class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums) # python repeats the 1 len(nums) times so if 4 numbers it becomes [1, 1, 1, 1]

        prefix = 1 # left side - the product of everything i have seen to my left 
        # we start with 1 because before the first number theres nothing 

        for i in range(len(nums)): # 0,1, 2, 3 - indexes of our flist 
            res[i] = prefix # so i = 0, res[0] = prefix (1)
            prefix *= nums[i] # getting ready for the next number 

            # after first loop - res = 1,1,2,8

        postfix = 1 # the product of everything to my right 

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res


        