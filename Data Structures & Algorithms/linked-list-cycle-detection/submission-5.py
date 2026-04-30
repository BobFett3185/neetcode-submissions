# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head #we set 2 ptrs a fast and slow one
        fast = head
        if not head: # if list is empty we return false
            return False

        while fast and fast.next: # while there are 2 next ones,move them and see if they cross
            current = current.next
            fast = fast.next.next
            
            if current == fast:
                return True
        # if theres not 2 more next ones, that means our link is finite so we can say false 
        
        return False

            