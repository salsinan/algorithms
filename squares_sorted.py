'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Constraints:
    1 <= nums.length <= 10^4
    -10^4 <= nums[i] <= 10^4
    nums is sorted in non-decreasing order.

'''

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        return sorted([x**2 for x in nums])

# Runtime: 246 ms
# Memory: 16.3 MB

# Tests:
soln = Solution()
print(soln.sortedSquares[-7,-3,2,3,11]) # [4,9,9,49,121]
print(soln.sortedSquares[-4,-1,0,3,10]) # [0,1,9,16,100]