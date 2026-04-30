# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        current = root
        # instead we can use binary search tree quality and search the correct side
        if p.val > current.val and q.val > current.val: # if both are greater 
            return self.lowestCommonAncestor(current.right, p,q) # then search right
        elif p.val < current.val and q.val < current.val: # if both are less
            return self.lowestCommonAncestor(current.left, p,q) # then search left
        else: # otherwise each are on opposite sides meaning we reached our LCA
            return current




#notes/thoughts

# we get 2 nodes and have to find their lowest common ancestor 
# maybe something like a rersion to search down -- do on left and right
# when we dont find both in our search from a node, then go back up and return that node

# maybe for a root, we search left and right subtrees and at each step we store the node.value in a hashmap 
# when we return, if the hashmap does not contain both numbers we return node.value
# nah this is actually overcomplicated