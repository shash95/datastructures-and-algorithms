"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""


class Solution:
    def lengthOfLIS(self, nums):
        if len(nums) == 0:
            return 0
        f = []
        # initialize array with 0
        for x in range(0, len(nums), 1):
            f.append(x)

        # traverse from end to start
        for i in range(len(nums)-1, -1, -1):
            current_lis = 1
            # traverse from current position to end
            for a in range(i, len(nums), 1):
                # check if any number to the right is greater than current numer
                if nums[a] > nums[i]:
                    # check if the LIS of the larger number is greater than current LIS
                    if current_lis <= f[a]:
                        current_lis = f[i] = f[a] + 1
            f[i] = current_lis
        # return the max number from the computed array
        return max(f)
