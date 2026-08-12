# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # basically are doing a bfs here 
        result = []
        queue = deque()
        queue.append(root)

        if not root: # edge case here
            return []

        while queue: # run bfs 
            result.append(queue[-1].val) # look at end of line and put in result
            iterations = len(queue) # keep this constant value
            for i in range(iterations):
                node = queue.popleft() # pop from queue and process that nodes children
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result

        