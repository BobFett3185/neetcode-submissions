# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        fast = head
        if not head:
            return False
        while current:
            current = current.next
            fast = fast.next
            if not fast:
                return False 
            fast = fast.next
            if not fast:
                return False

            if current == fast:
                return True

            