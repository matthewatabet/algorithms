class TreeNode(object):

    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x

    def __repr__(self):
        return str(self.val)

    def add(self, v):
        if v > self.val:
            if self.right is None:
                self.right = TreeNode(v)
            else:
                self.right.add(v)
        else:
            if self.left is None:
                self.left = TreeNode(v)
            else:
                self.left.add(v)


class Solution(object):

    def postorderTraversal(self, root):
        if root is None:
            return []

        current = root
        stack = []
        result = []
        visited = set([])

        while current is not None:
            if current.left is not None and current.left not in visited:
                stack.append(current)
                current = current.left

            elif current.right is not None and current.right not in visited:
                stack.append(current)
                current = current.right

            else:
                result.append(current.val)
                visited.add(current)

                try:
                    current = stack.pop()
                except IndexError:
                    current = None
        return result


def main():
    root = TreeNode(5)
    root.add(6)
    root.add(7)
    root.add(2)

    print Solution().postorderTraversal(root)

    root = TreeNode(3)
    print Solution().postorderTraversal(root)
if __name__ == '__main__':
    main()
