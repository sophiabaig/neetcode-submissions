# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        q = collections.deque()
        result = []
        q.append(root)
        output = []

        while q:
            q_len = len(q)
            level = []

            for i in range(q_len):
                node = q.popleft()

                if node:
                    level.append(node.val)
                    if node.left: q.append(node.left)
                    if node.right: q.append(node.right)

                if node and i == (q_len - 1):
                    output.append(node.val)

            if level:
                result.append(level)

        return output

