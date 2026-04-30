# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        # we basically do a BFS with this 
        q = collections.deque() # get a queue
        q.append(root)

        while q:# while there is something 
            level = [] #empty array to keep our result in 
            n = len(q)
            for i in range(n):
                node = q.popleft()# we pop from the queue n times where n is the length of q
                if node:
                    level.append(node.val) # add to level intermediate array 
                    q.append(node.left)
                    q.append(node.right)
            if level:
                result.append(level)


        return result


