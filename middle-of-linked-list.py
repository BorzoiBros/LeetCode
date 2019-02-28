# https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        linked_list_length = 0
        ans = head
        while head is not None:
            head = head.next
            linked_list_length += 1
        middle_index = round(linked_list_length/2)
        while  middle_index > 0:
            ans = ans.next
            middle_index -= 1
        return ans        