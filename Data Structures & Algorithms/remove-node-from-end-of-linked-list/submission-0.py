# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) # node before head 
        left = dummy
        right = head

        for i in range(n): # we shift right by n places
            right = right.next
        # now left and right are seperated by n spots 

        while right:# now we can move the left and right --> until right is at the end 
            left = left.next
            right = right.next

        left.next = left.next.next # skip over removed node 
        return dummy.next # return head


        # dummy node and 2 ptr with linked list
