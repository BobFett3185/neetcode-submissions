# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        start = ListNode()
        node3 = start

        node1 = list1
        node2= list2
        while node1 and node2:
            if node1.val < node2.val:
                node3.next = node1
                node1 = node1.next
                node3 = node3.next
            else:
                node3.next = node2
                node2 = node2.next
                node3 = node3.next
        while node1:
            node3.next = node1
            node1 = node1.next
            node3 = node3.next
        while node2:
            node3.next = node2
            node2 = node2.next
            node3 = node3.next
        return start.next


                