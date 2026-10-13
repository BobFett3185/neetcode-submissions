# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # do a level order traversal and only add the last node 
        queue = deque()
        result = []
        if not root:
            return []
        queue.append(root)
        # we pop from the root and append only the last one in the for loop 
        while len(queue)>0:
            iterations = len(queue)
            for i in range(iterations):
                node = queue.popleft()
                if i == iterations-1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result
