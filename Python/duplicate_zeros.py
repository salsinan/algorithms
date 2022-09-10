
'''
Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

Constraints:

    1 <= arr.length <= 104
    0 <= arr[i] <= 9
'''

# Runtime: 74 ms
# Memory Usage: 14.8 MB
class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        """ 
            Iterate over array to find zeros
            if a zero is found, insert a zero at the next index and remove the               last element.
            Jump over the inserted zero on the next iteration
        """
        i = 0
        
        while i < len(arr) - 1:
            if arr[i] == 0:
                arr.insert(i+1, 0)
                arr.pop()
                i += 1
            i += 1
        return arr

soln = Solution()
print(soln.duplicateZeros([1,0,2,3,0,4,5,0])) #[1,0,0,2,3,0,0,4]
print(soln.duplicateZeros([1,2,3])) #[1,2,3]