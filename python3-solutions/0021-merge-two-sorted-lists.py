# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        merged_list = ListNode()
        pos = merged_list

        while list1 and list2:
            if list1.val < list2.val:
                pos.next = list1
                list1 = list1.next
            else:
                pos.next = list2
                list2 = list2.next

            pos = pos.next

        if list1:
            pos.next = list1
        elif list2:
            pos.next = list2

        return merged_list.next
