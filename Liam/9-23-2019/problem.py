from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node):
    # base case
    if node == None:
        return ''

    # recursive case
    return node.val + ' ' + serialize(node.left) + serialize(node.right)


def deserialize(str):
    # call helper recursive function
    return deserialize_deque(deque(str.split()))


def deserialize_deque(strDeque):
    # base case
    if len(strDeque) == 0:
        return None

    # recursive case
    return Node(strDeque.popleft(), deserialize_deque(strDeque), deserialize_deque(strDeque))


def main():
    # example test code from problem
    #        (root)
    #         /  \
    #    (left)  (right)
    #      /
    # (left.left)
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'


if __name__ == '__main__':
    main()