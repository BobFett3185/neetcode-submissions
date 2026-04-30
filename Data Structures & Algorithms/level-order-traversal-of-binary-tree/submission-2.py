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
        if not root:
            return result
        q.append(root)

        while q:# while there is something 
            level = [] #empty array to keep our result in 
            n = len(q)
            for i in range(n):
                node = q.popleft()# we pop from the queue n times where n is the length of q
                level.append(node.val) # add to level intermediate array 
                if node.left:
                    q.append(node.left) # we add the left subroot 
                if node.right:
                    q.append(node.right) # and the right subroot
            result.append(level) # then add it to result


        return result


