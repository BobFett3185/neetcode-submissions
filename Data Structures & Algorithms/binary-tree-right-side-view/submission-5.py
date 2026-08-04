# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return []
        queue = deque([root])
        
        while queue:
            result.append(queue[-1].val)# add the rightmost element of that level

            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result 



'''
we can only return one element per level 
so do some kind of breadth first search i think and at each level, add the last element in the queue to the result
'''


