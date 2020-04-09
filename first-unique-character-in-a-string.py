# 387. First Unique Character in a String
# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

# Examples:
#     s = "leetcode"
#     return 0.

#     s = "loveleetcode",
#     return 2.
# Note: You may assume the string contain only lowercase letters.


class Solution:
    def firstUniqChar(self, s: str) -> int:
        # build hash map : character and how often it appears
        count = collections.Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1
        
# My first solution
#         char_count = {}
#         for char in s:
#             if char not in char_count:
#                 char_count[char] = 1
#             else:
#                 char_count[char] += 1
        
#         for idx, char in enumerate(s):
#             if char_count[char] == 1:
#                 return idx
#         return -1
