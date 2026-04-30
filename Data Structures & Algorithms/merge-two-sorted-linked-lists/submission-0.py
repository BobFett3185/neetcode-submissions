# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        current1 = list1 # this is the ptr to nodes in list1
        current2 = list2 # ptr to nodes in list2

        dummy = node = ListNode() # create a new node to start our new chain
        # dummy node for keeping intermediate?

        # always mess with the next one not the value
        # compare which is smaller until 1 list is empty
        while current1 and current2:
            if current1.val < current2.val:
                node.next = current1 # set the next node 
                node = node.next # move to next node
                current1 = current1.next # move current node 
            else:
                node.next = current2
                node = node.next 
                current2 = current2.next

        # after this is over one list will have remaining
        node.next = current1 or current2
        return dummy.next


        # we go through