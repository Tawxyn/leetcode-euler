class Solution(object):
    def maxDepth(self, root):
        
        if root is None:
            return 0
        else:
            maxLeft = self.maxDepth(root.left)
            maxRight = self.maxDepth(root.right)
            return 1 + max(maxLeft, maxRight)
