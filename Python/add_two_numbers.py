'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Constraints:

    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.
'''

# Runtime: 78 ms
# Memory Usage: 13.9 MB

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Converts a linked list into an integer, with the tail as the leading digit
    def to_int(self, l1:ListNode):
        num = 0
        current_val = l1
        counter = 1 # keeps track of place value
        
        while current_val:
            num += (current_val.val * counter)
            current_val = current_val.next
            counter *= 10
        return num
    
    
    # Converts an integer into a linked list, with the leading digit as the tail
    def to_linked_list(self, num):
        
        result_node = None
        
        for n in (reversed_num := str(num)[::-1]):
            if result_node is None:
                result_node = ListNode(n)
                current_node = result_node
            else:
                current_node.next = ListNode(n)
                current_node = current_node.next 
                
        return result_node
    
    # Returns a linked list representing the sum of two linked lists
    def addTwoNumbers(self, l1:ListNode, l2:ListNode) -> ListNode:
        num_1 = self.to_int(l1)
        num_2 = self.to_int(l2)
        return self.to_linked_list(num_1 + num_2)

# Runtime: 78 ms
# Memory Usage: 13.9 MB

# Plug in to test
# https://leetcode.com/problems/add-two-numbers/