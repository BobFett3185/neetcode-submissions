# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # have fast and slow ptr to split the list 

        slow, fast = head, head.next # set up fast and slow pointer
        while fast and fast.next: # move them 
            slow = slow.next
            fast = fast.next.next
       
        # reverse the second half from slow to the end 
        current = slow.next # this is the start of the second half
        prev =  slow.next  = None # set a prev and break the conneciton between lists
        while current: # reverse logic
            temp = current.next 
            current.next = prev 
            prev = current
            current = temp

        # now we merge 
        first, second = head, prev 
        while second:
            temp1, temp2 = first.next, second.next # keep some temps
            first.next = second 
            second.next = temp1
            first, second = temp1 , temp2
        

        


        
        