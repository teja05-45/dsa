class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1

        max_water = 0
        while left < right:
            min_line = min(height[left], height[right])
            water = min_line * (right - left)
            if water > max_water:
                max_water = water
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water


           