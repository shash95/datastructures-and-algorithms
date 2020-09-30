"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines
are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""
class Solution:
    def maxArea(self, height):
        max_vol = 0
        low = 0
        high = len(height)-1
        while low < high:
            max_vol = max(min(height[low], height[high]) * (high-low), max_vol)
            if height[low] < height[high]:
                low += 1
            else:
                high-=1

        return max_vol
