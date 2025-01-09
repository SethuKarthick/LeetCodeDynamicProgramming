# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        if root1 is None:
            return root2

        root1Stack = [root1]
        root2Stack = [root2]

        while len(root1Stack) > 0:
            rootNode1 = root1Stack.pop()
            rootNode2 = root2Stack.pop()

            if rootNode2 is None:
                continue

            rootNode1.val += rootNode2.val

            if rootNode1.left is None:
                rootNode1.left = rootNode2.left
            else:
                root1Stack.append(rootNode1.left)
                root2Stack.append(rootNode2.left)
            
            if rootNode1.right is None:
                rootNode1.right = rootNode2.right
            else:
                root1Stack.append(rootNode1.right)
                root2Stack.append(rootNode2.right)
        return root1


        