# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorderIndex = 0
        inorderMap = {value: i for i, value in enumerate(inorder)}
        # map values to index
        def build(inorder, start, end):
            nonlocal preorderIndex
            if start>end:
                return
            
            root = TreeNode(preorder[preorderIndex])
            preorderIndex +=1 
            
            index = inorderMap[root.val]

            root.left = build(inorder, start, index-1)
            root.right = build(inorder, index+1, end)
            return root
        return build(inorder, 0, len(inorder)-1)


            

            



