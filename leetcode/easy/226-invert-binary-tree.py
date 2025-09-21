class Solution(object):
    def invertTree(self, root):
        if root is None:
            return None
        else:
            self.invertTree(root.left)
            self.invertTree(root.right)
            root.left, root.right = root.right, root.left
            return root
