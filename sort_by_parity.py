'''
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

Constraints:

    1 <= nums.length <= 5000
    0 <= nums[i] <= 5000
'''
# Runtime: 79 ms
# Memory Usage: 14.6 MB

class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        add_idx = 0
        
        for n in range(len(nums)):
            if (curr := nums[n]) %2 == 0:
                nums[n] = nums[add_idx]
                nums[add_idx] = curr
                add_idx += 1
        return nums

soln = Solution()
print(soln.sortArrayByParity([3,1,2,4])) # [2,4,3,1]
print(soln.sortArrayByParity([0])) # [0]