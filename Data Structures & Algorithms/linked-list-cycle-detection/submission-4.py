# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head #
        fast = head
        if not head:
            return False
        while fast and fast.next:
            current = current.next
            fast = fast.next.next
            
            if current == fast:
                return True
        return False

            