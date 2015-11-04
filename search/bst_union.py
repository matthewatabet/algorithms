from bst import BinarySearchTree


def _inorder(node, flattened):
    if node is None:
        return
    _inorder(node.left, flattened)
    flattened.append(node.key)
    _inorder(node.right, flattened)


def inorder(tree):
    '''
    Return a flattened version of tree as a list, using in order traversal.
    '''
    f = []
    _inorder(tree, f)
    return f


def diff(a_tree, b_tree):
    '''
    Return a list of keys in a but not in b.
    '''
    a_keys = inorder(a_tree.root)
    b_keys = inorder(b_tree.root)
    i = 0
    j = 0
    diff = []

    while i < len(a_keys):
        while j < len(b_keys) and b_keys[j] < a_keys[i]:
            j += 1
        if a_keys[i] != b_keys[j]:
            diff.append(a_keys[i])
        i += 1
    return diff


def main():

    a = BinarySearchTree()
    a.add(2, '')
    a.add(1, '')
    a.add(4, '')
    a.add(5, '')

    b = BinarySearchTree()
    b.add(5, '')
    b.add(2, '')
    b.add(3, '')

    print diff(a, b)


if __name__ == '__main__':
    main()
