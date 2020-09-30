"""
Given a string s, find the length of the longest substring without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0 or len(s) == 1:
            return len(s)

        start = 0
        end = 0
        character_list = []
        max_length = 1
        while True:
            if start == len(s):
                return max(max_length, len(character_list))
            end = start
            while True:
                if end == len(s):
                    max_length = max(max_length, len(character_list))
                    break
                if s[end] in character_list:
                    max_length = max(max_length, len(character_list))
                    character_list = []
                    break
                else:
                    character_list.append(s[end])
                    end += 1

            start += 1
