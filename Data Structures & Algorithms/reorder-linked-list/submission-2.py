# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # get the second half 
        # then reverse it
        # then merge with our first half 
        dummy = ListNode()
        dummy.next = head

        fast = head 
        slow = dummy 
        while fast and fast.next:
            fast = fast.next.next 
            slow = slow.next 
        
        # now we should have start of second half at slow, reverse it 
        start = slow.next 
        slow.next = None

        prev = None
        curr = start
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        tail = None
        # merge with head 
        while head and prev:
            next1 = head.next 
            next2 = prev.next
            head.next = prev
            prev.next = next1
            tail = prev 
            head = next1
            prev = next2
            
        if prev:
            tail.next = prev
        
        
        
        





