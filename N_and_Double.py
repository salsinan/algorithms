'''
Given an array arr of integers, check if there exist two indices i and j such that :

    i != j
    0 <= i, j < arr.length
    arr[i] == 2 * arr[j]

Constraints:

    2 <= arr.length <= 500
    -10^3 <= arr[i] <= 10^3

'''
# Runtime: 63 ms
# Memory Usage: 13.9 MB

class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        nums = set()
        
        for n in arr:
            half = n // 2 if n % 2 == 0 else None
            
            if n * 2 in nums or half in nums:
                return True

            nums.add(n)
        return False

soln = Solution()
print(soln.checkIfExist([10,2,5,3])) # True
print(soln.checkIfExist([3,1,7,11])) # False