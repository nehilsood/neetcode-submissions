# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict,deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = defaultdict(list)
        level = 0
        if not root: return []
        queue = deque([root])
        while queue:
            level += 1
            qlen = len(queue)
            # print(qlen)
            for _ in range(qlen):
                node = queue.popleft()
                result[level].append(node.val)
                # print(level,node.val)
                if node.left:
                    queue.append(node.left)
                    print(node.left.val)
                if node.right:
                    queue.append(node.right)
                    print(node.right.val)
        return list(result.values())

            





        