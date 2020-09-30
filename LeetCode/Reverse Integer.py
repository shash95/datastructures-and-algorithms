"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
"""


class Solution:
    def reverse(self, x: int) -> int:

        negative = False
        if x < 0:
            x *= -1
            negative = True
        r = 0
        while (x != 0):
            r = r * 10 + x % 10
            x = int(x / 10)

        if r > 2 ** 31 - 1:
            r = 0
        if negative:
            r *= -1

        return r

