# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorderIndex = 0
        inorderMap = {value: i for i, value in enumerate(inorder)} # for efficiency

        def build(start, end): # use start and end to know chunk of inorder 
            nonlocal preorderIndex
            if start>end: # base case
                return
            
            root = TreeNode(preorder[preorderIndex]) # create a node
            preorderIndex +=1  # increment element 
            
            index = inorderMap[root.val] # split up your inorder into sections
            # call left and right children 
            root.left = build(start, index-1) 
            root.right = build( index+1, end)
        
            return root
        return build(0, len(inorder)-1)


            

            



