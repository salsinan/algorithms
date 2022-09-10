'''
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Constraints:

    0 <= nums.length <= 100
    0 <= nums[i] <= 50
    0 <= val <= 100
'''
# Runtime: 35 ms
# Memory Usage: 13.9 MB

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        count = 0
        length = len(nums)
        swap_idx = length - 1

        i = 0
        while i < length:
            curr = nums[i]
            if curr == val and swap_idx >= i:
                # Swap the first and kth element
                nums[i] = nums[swap_idx]
                nums[swap_idx] = curr
                swap_idx -= 1
                # Increment number of swaps, this will determine the final length
                count += 1

            else:
                # Only increment i once the current element != val
                i += 1
        print(nums[:length-count])
        return length - count

soln = Solution()
print(soln.removeElement([3,2,2,3], 3)) # 2
# [2,2]
# 2
print(soln.removeElement([0,1,2,2,3,0,4,2], 2)) # 5
# [0,1,4,0,3]
# 5