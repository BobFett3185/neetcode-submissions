# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        '''
        Draw out trees to see why we do it this way, makes it much easier

        basically we go through the pre order traversal and build subtrees recursively 
        problem is we dont know which part of the preorder is the left or right subtree

        inorder has root in the middle, so if you find the index of the root you can 
        figure out the sizes of the left and right subarrays in the in preorder array 

        Then we split up the pre order arrays and run the same algorithm on those subtrees
        '''
        
        if not preorder or not inorder:
            return None 
        root = TreeNode(preorder[0]) # start our tree with the root 
        

        # now we do recursively 
        mid = inorder.index(preorder[0]) # we get mid from the inorder traversal 
        root.left = self.buildTree(preorder[1:mid+1], inorder[0:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root

        



        