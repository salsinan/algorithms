'''
Given an array nums of integers, return how many of them contain an even number of digits.

Constraints:

    1 <= nums.length <= 500
    1 <= nums[i] <= 10^5
'''

# Runtime: 55 ms
# Memory Usage: 14 MB

class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        evens = 0
        
        for num in nums:
            evens += 1 if len(str(num)) % 2 == 0 else 0
        return evens

soln = Solution()
print(soln.findNumbers([12,345,2,6,7896])) # 2
print(soln.findNumbers([555,901,482,1771])) # 1