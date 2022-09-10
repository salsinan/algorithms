'''
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

Constraints:

    1 <= nums.length <= 10^4
    -2^31 <= nums[i] <= 2^31 - 1
'''
# Solution-1
    # Runtime: 53 ms
    # Memory: 16 MB

# class Solution:
#     def thirdMax(self, nums: list[int]) -> int:
#         num_set = set(nums)

#         if len(num_set) < 3:
#             return max(nums)

#         first = second = third = -2e33

#         for n in set(nums):
#             if n > first:
#                 third = second
#                 second = first
#                 first = n
#             elif n > second:
#                 third = second
#                 second = n
#             elif n > third:
#                 third = n
#         return third


# Solution-2:
    # Runtime: 61 ms
    # Memory: 15.5 MB
    
class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        nums = sorted(set(nums))
        
        return max(nums) if len(nums) < 3 else nums[-3]

# Tests:
soln = Solution()
print(soln.thirdMax([3,2,1])) # 1
print(soln.thirdMax([1,2])) # 2
print(soln.thirdMax([2,2,3,1])) # 1
