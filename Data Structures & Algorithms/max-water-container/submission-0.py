class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0

        left, right = 0, len(heights) - 1

        while left < right:
            area = (right - left) * min(heights[left], heights[right]) #width * height 

            result = max(result, area) # is this container better than the best one I've seen before?

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return result
