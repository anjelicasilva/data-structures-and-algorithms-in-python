# 344. Reverse String (Leet Code)

# Write a function that reverses a string. 
# The input string is given as an array of characters char[].
# Do not allocate extra space for another array, 
# you must do this by modifying the input array in-place with O(1) extra memory.

# You may assume all the characters consist of printable ascii characters.

# Example 1:
#     Input: ["h","e","l","l","o"]
#     Output: ["o","l","l","e","h"]
# Example 2:
#     Input: ["H","a","n","n","a","h"]
#     Output: ["h","a","n","n","a","H"]


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        front_idx = 0
        last_idx = len(s)-1     
            
        while front_idx < last_idx:
            s[front_idx], s[last_idx] = s[last_idx], s[front_idx]
            front_idx += 1
            last_idx-=1  
            
            
        # Another way to solve
        # while front_idx < last_idx:
        #     holder = s[front_idx]
        #     s[front_idx] = s[last_idx]
        #     s[last_idx] = holder
        #     front_idx += 1
        #     last_idx-=1  