# 844. Backspace String Compare (Easy)

# Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

# Example 1:
#     Input: S = "ab#c", T = "ad#c"
#     Output: true
    
#     Explanation: Both S and T become "ac".

# Example 2:
#     Input: S = "ab##", T = "c#d#"
#     Output: true
    
#     Explanation: Both S and T become "".

# Example 3:
#     Input: S = "a##c", T = "#a#c"
#     Output: true
    
#     Explanation: Both S and T become "c".

# Example 4:
#     Input: S = "a#c", T = "b"
#     Output: false
#     Explanation: S becomes "c" while T becomes "b".

# Note:
#     1 <= S.length <= 200
#     1 <= T.length <= 200
#     S and T only contain lowercase letters and '#' characters.

# Follow up:
#     Can you solve it in O(N) time and O(1) space?


# class Solution:
    
#     def create_new_string(self, string):
#             new_string_lst = []
#             for letter in string:
#                 if letter != '#':
#                     new_string_lst.append(letter)
#                 elif new_string_lst == []:
#                     continue
#                 elif new_string_lst:
#                     new_string_lst.pop()
#             return "".join(new_string_lst)
    
#     def backspaceCompare(self, S: str, T: str) -> bool:  

#         return self.create_new_string(S) == self.create_new_string(T)



# Another Solution
def create_stack(string):
    new_stack = []
    for char in string:
        if char == "#" and new_stack:
            new_stack.pop()
        elif char == "#":
            continue
        else:
            new_stack.append(char)
    return new_stack

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s_stack = create_stack(S)
        t_stack = create_stack(T)
        return s_stack == t_stack