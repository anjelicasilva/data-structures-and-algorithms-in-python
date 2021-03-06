# 1323. Maximum 69 Number (Easy)

# Given a positive integer num consisting only of digits 6 and 9.

# Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

# Example 1:
#     Input: num = 9669
#     Output: 9969
    
#     Explanation: 
#     Changing the first digit results in 6669.
#     Changing the second digit results in 9969.
#     Changing the third digit results in 9699.
#     Changing the fourth digit results in 9666. 
#     The maximum number is 9969.

# Example 2:
#     Input: num = 9996
#     Output: 9999
    
#     Explanation: Changing the last digit 6 to 9 results in the maximum number.

# Example 3:
#     Input: num = 9999
#     Output: 9999
    
#     Explanation: It is better not to apply any change.
 
# Constraints:
#     1 <= num <= 10^4
#     num's digits are 6 or 9.


class Solution:
    def maximum69Number (self, num: int) -> int:
        num_string = str(num)
        string_length = len(num_string)
        
        for idx in range(0,string_length):
            if num_string[idx] == "6":
                power = (string_length - idx - 1)
                num = num + (3*(10**power))
                return num
            idx += 1
        return num


# ANOTHER SOLUTION
# class Solution:
#     def maximum69Number (self, num: int) -> int:
#         number_str = str(num)
        
#         idx = 0
#         for number in number_str:
#             if number == "6":
#                 new_string = number_str[:idx] + "9" + number_str[idx+1:]
#                 return int(new_string)
#             idx += 1
#         return num