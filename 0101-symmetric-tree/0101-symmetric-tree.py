# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        stackLeft = [root.left]
        stackRight = [root.right]

        while len(stackLeft) > 0:
            left = stackLeft.pop()
            right = stackRight.pop()

            if left is None and right is None:
                continue 

            if left is None or right is None or left.val != right.val:
                return False
            
            stackLeft.append(left.left)
            stackLeft.append(left.right)
            stackRight.append(right.right)
            stackRight.append(right.left)

        return True