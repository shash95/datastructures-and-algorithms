"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

import sys
class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        lcp = ""
        current_char = None
        i = 0
        min_length = sys.maxsize
        for a in strs:
            min_length = min(len(a), min_length)
        match = True
        while i < min_length:
            current_char = strs[0][i]
            for x in range(0, len(strs), 1):

                if strs[x][i] != current_char:
                    match = False
                    break
            if not match:
                break
            lcp = lcp + current_char
            i+=1
        return lcp