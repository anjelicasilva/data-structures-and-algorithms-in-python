# 560. Subarray Sum Equals K (Medium)

# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

# Example 1:
#     Input:nums = [1,1,1], k = 2
#     Output: 2
# Note:
#     The length of the array is in range [1, 20,000].
#     The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for starting_idx in range(0, len(nums)):
            current_idx = starting_idx
            current_sum = nums[current_idx]
            if current_sum == k:
                    count += 1
            for current_idx in range(current_idx+1, len(nums)):
                current_sum += nums[current_idx] 
                if current_sum == k:
                    count += 1
        return count