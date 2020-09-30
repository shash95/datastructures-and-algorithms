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
