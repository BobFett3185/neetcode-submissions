# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head # start with current

        # draw out the linkedlist and see what you need
        # you need a previous, current, temp
        # iterate through

        while current: #starting with head
            temp = current.next  #set a temporary 
            current.next = prev #set our next pointer to the previous pointer
            prev = current #now our previous pointer for next iteration is our current rn 
            current = temp #now we move to the next elemnt which was stored either
        
        return prev #return last element which is our new head



