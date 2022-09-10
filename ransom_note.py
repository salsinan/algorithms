'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Constraints:

    1 <= ransomNote.length, magazine.length <= 105
    ransomNote and magazine consist of lowercase English letters.

'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return all(ransomNote.count(ch) <= magazine.count(ch) for ch in set(ransomNote))


# Tests:
soln = Solution()
print(soln.canConstruct("aa", "aab")) # True
print(soln.canConstruct("aa", "ab")) # False
print(soln.canConstruct("hello", "aloha")) # False
print(soln.canConstruct("hello", "allohale")) # True
print(soln.canConstruct("", "")) # True
print(soln.canConstruct("", "aab")) # True

# Runtime = 38ms
# Memory = 14.1 MB
