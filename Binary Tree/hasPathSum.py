def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    stack = [(root, sum)]
    while len(stack) > 0:
        node, tmp_sum = stack.pop()
        if node:
            if not node.left and not node.right and node.val == tmp_sum:
                return True
            stack.append((node.right, tmp_sum-node.val))
            stack.append((node.left, tmp_sum-node.val))
    return False