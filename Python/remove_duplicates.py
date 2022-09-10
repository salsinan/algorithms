'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}

If all assertions pass, then your solution will be accepted.

Constraints:

    1 <= nums.length <= 3 * 10^4
    -100 <= nums[i] <= 100
    nums is sorted in non-decreasing order.
'''

# Runtime: 94 ms
# Memory Usage: 15.6 MB

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        unique_idx = 1 # The index to add next unique element
        curr = nums[0] # The current unique element

        for n in nums[1:]:
            if n != curr:
                curr = nums[unique_idx] = n
                unique_idx += 1
        print(nums[:unique_idx])
        return unique_idx

soln = Solution()
print(soln.removeDuplicates([1,1,2])) # 2
# [1,2]
# 2
print(soln.removeDuplicates([0,0,1,1,1,2,2,3,3,4])) # 5
# [0,1,2,3,4]
# 5