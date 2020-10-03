"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Follow up: The overall run time complexity should be O(log (m+n)).



Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
Example 4:

Input: nums1 = [], nums2 = [1]
Output: 1.00000
Example 5:

Input: nums1 = [2], nums2 = []
Output: 2.00000

"""
class Solution:
    def median(self, arr):
        mid = int(len(arr)/2)
        if len(arr)%2 != 0:
            return arr[mid]
        return (arr[mid] + arr[mid-1])/2

    def findMedianSortedArrays(self, nums1, nums2):
        nums = []
        i = i1 = i2 = 0
        while i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1] < nums2[i2]:
                nums.append(nums1[i1])
                i1 += 1
            else:
                nums.append(nums2[i2])
                i2 += 1

        if i1 < len(nums1):
            while i1 < len(nums1):
                nums.append(nums1[i1])
                i1 += 1

        if i2 < len(nums2):
            while i2 < len(nums2):
                nums.append(nums2[i2])
                i2 += 1

        # print(nums)
        return self.median(nums)
