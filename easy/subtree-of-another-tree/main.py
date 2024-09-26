from typing import Optional


class TreeNode:
    """Definition for a binary tree node"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    def sameTree(self,q,p):
        if not q and not p:
            return True

        if q and p and q.val == p.val:
            return (self.sameTree(q.left, p.left) and self.sameTree(p.right, q.right))

        return False