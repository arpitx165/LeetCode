# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3290/

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        while head and fast and fast.next:
            head = head.next
            fast = fast.next.next    
        return head    
        