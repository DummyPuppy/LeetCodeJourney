# find minimum absolute difference in BST
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        minabs = 1000001


        def inorder(node,absdiff) ->int :
            if not node:
                return absdiff
            else:
                l = node.left
                while l and l.right:
                    l = l.right
                r = node.right
                while r and r.left:
                    r = r.left
                absdiff = min(absdiff,mad(node,l), mad(node,r))
                absdiff = inorder(node.left,absdiff)
                absdiff = inorder(node.right,absdiff)
            return absdiff
                    
             
        def mad(curr,next) -> int:
            if curr and next:
                return abs(curr.val - next.val)
            else:
                return 100001


        curr = root
        result = inorder(curr,minabs)
        return result

                
