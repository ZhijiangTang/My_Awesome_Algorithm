# Leetecode

# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

# 有效 二叉搜索树定义如下：

# 节点的左子树只包含 小于 当前节点的数。
# 节点的右子树只包含 大于 当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    
class Solution:
    def isValidBST(self, root: Optional[TreeNode],) -> bool:
        result,_,_ = self.search(root)
        return result

    def search(self, root: Optional[TreeNode]):
        if root.left is None and root.right is None:
            return True,float("inf"),-float("inf")
        left_result = True
        right_result = True
        root_min = float("inf")
        root_max = -float("inf")
        if root.left is not None:
            if root.val > root.left.val :
                left_result,left_min,left_max = self.search(root.left)
                if left_max >= root.val:
                    return False,float("inf"),-float("inf")
                root_min = min(root.left.val,left_min)
            else:
                return False,-float("inf"),float("inf") 
        if root.right is not None:
            if root.val < root.right.val:
                right_result,right_min,right_max = self.search(root.right)
                if right_min <= root.val:
                    return False,float("inf"),-float("inf")
                root_max = max(root.right.val, right_max)
            else:
                return False,float("inf"),-float("inf")
        return left_result & right_result, root_min, root_max

if __name__ == "__main__":

    pass

        