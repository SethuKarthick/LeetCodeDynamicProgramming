# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.values = set()
        q = deque()
        q.append((root,0))
        while q:
            n = len(q)
            for _ in range(n):
                node, cur_val = q.popleft()
                node.val = cur_val
                self.values.add(cur_val)
                if node.left:
                    q.append((node.left,2*cur_val + 1))
                if node.right:
                    q.append((node.right,2*cur_val + 2))
        

        

    def find(self, target: int) -> bool:
        return target in self.values

        # if target in self.values:
        #     return True
        # return False

    # def __init__(self, root):
    #     self.values = set()
    #     self.recover_tree(root, 0)

    # def recover_tree(self, node, value):
    #     if not node:
    #         return
    #     self.values.add(value)
    #     node.val = value
    #     self.recover_tree(node.left, 2 * value + 1)
    #     self.recover_tree(node.right, 2 * value + 2)

    # def find(self, target):
    #     return target in self.values
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)