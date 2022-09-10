'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Constraints:

    1 <= nums.length <= 10^4
    -2^31 <= nums[i] <= 2^31 - 1
'''

# Runtime: 176 ms
# Memory Usage: 15.6 MB

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        add_idx = 0 # Index to which to add nonzero elements

        for n in range(len(nums)):
            if (curr := nums[n]) != 0:
                nums[n] = 0
                nums[add_idx] = curr
                add_idx += 1

        return nums

soln = Solution()
print(soln.moveZeroes([0,1,0,3,12])) # [1,3,12,0,0]
print(soln.moveZeroes([0])) # [0]