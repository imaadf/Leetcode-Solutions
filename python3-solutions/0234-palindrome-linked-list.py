# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow_prev = None

        while slow:
            tmp = slow.next
            slow.next = slow_prev
            slow_prev = slow
            slow = tmp

        start, end = head, slow_prev

        while end:
            if start.val != end.val:
                return False
            start = start.next
            end = end.next

        return True
