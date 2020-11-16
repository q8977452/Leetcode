def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def dfs(root):
            if root is None:
                return []
            if root is not None:
                dfs(root.left) 
                dfs(root.right)
                res.append(root.val)
        dfs(root)
        return res