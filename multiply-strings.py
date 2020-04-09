# 43. Multiply Strings (Medium)

# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

# Example 1:
#     Input: num1 = "2", num2 = "3"
#     Output: "6"

# Example 2:
#     Input: num1 = "123", num2 = "456"
#     Output: "56088"

# Note:
#     The length of both num1 and num2 is < 110.
#     Both num1 and num2 contain only digits 0-9.
#     Both num1 and num2 do not contain any leading zero, except the number 0 itself.
#     You must not use any built-in BigInteger library or convert the inputs to integer directly.

class Solution:
    def build_num(self, num):
        num_dict = {
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "0": 0,
        }
        
        num_length = len(num) - 1
        
        number = 0
        
        for char in num:
            sum = num_dict[char] * (10**num_length)
            num_length -= 1
            number = number + sum
        return number
    
    
    def multiply(self, num1: str, num2: str) -> str:
        num1 = self.build_num(num1)
        num2 = self.build_num(num2)
        return str(num1 * num2)