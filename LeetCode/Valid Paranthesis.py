"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""

class Solution:
    def isValid(self, s):
        if s == "":
            return True
        open_bracket_list = ['(', '{', '[']
        close_bracket_list = [')', '}', ']']
        open_to_close_mapping = {']': '[', '}': '{', ')': '('}
        char_list = []
        for a in s:
            if a in open_bracket_list:
                char_list.append(a)
                continue
            # return false if list is already empty and a closing paranthesis is found
            elif len(char_list) == 0:
                return False
            elif char_list[len(char_list) - 1] != open_to_close_mapping[a]:
                return False
            # remove last character if matching opening paranthesis was found
            char_list.pop(len(char_list)-1)
        if len(char_list) != 0:
            return False
        return True

if __name__ == '__main__':
    s = "()("
    x = Solution().isValid(s)
    print(x)