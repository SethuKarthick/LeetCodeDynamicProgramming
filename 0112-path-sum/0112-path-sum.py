# Definition for a binary tree node.
from collections import deque

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        deq = deque()
        deq.append((root, sum))
        while deq:
            node, curr_sum = deq.popleft()
            if not node:
                continue
            if not node.left and not node.right and curr_sum == node.val:
                return True
            deq.append((node.left, curr_sum - node.val))
            deq.append((node.right, curr_sum - node.val))
        return False
#     def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
#         stack = [(root, sum)]

#         while stack:
#             node, currentSum = stack.pop()

#         if not node:
#             continue

#         if not node.left and node.right and currentSum == node.val:
#             return True
        
#         stack.append([node.left, currentSum - node.val])
#         stack.appedn([node.right, currentSum - node.val])

#         return False


