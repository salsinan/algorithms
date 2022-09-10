
'''
Given an array of integers arr, return true if and only if it is a valid mountain array.

Constraints:

    1 <= arr.length <= 10^4
    0 <= arr[i] <= 10^4
'''

# Runtime: 261 ms
# Memory Usage: 15.4 MB

class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        last_idx = len(arr) - 1
        top = 0

        # Check that arr is in ascending order
        while top < last_idx and arr[top] < arr[top + 1]:
            top += 1

        # If the peak is at the beginning or end
        if top == 0 or top == last_idx:
            return False

        # Check that arr is in descending order till the end
        while top < last_idx and arr[top] > arr[top + 1]:
            top += 1

            if top == last_idx:
                return True
        return False

# Tests:
soln = Solution()
print(soln.validMountainArray([2,1])) # False
print(soln.validMountainArray([3,5,5])) # False
print(soln.validMountainArray([0,3,2,1])) # True
