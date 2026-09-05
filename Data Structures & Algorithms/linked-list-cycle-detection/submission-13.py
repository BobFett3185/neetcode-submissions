# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node1 = head 
        node2 = head 
        if not head or not head.next or not head.next.next:
            return False
        while node2.next:
            node1 = node1.next
            node2 = node2.next.next
            if not node2:
                break
            if node1 == node2:
                return True 
        return False