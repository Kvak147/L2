import matplotlib.pyplot as plt
import numpy as np
from collections import deque

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.parent = None
        self.val = key
        self.color = 'red'

class RedBlackTree:
    def __init__(self):
        self.TNULL = TreeNode(0)
        self.TNULL.color = 'black'
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL

    def insert(self, key):
        node = TreeNode(key)
        node.parent = None
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 'red'

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.val < x.val:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y == None:
            self.root = node
        elif node.val < y.val:
            y.left = node
        else:
            y.right = node

        if node.parent == None:
            node.color = 'black'
            return

        if node.parent.parent == None:
            return

        self._fix_insert(node)

    def _fix_insert(self, k):
        while k.parent.color == 'red':
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 'red':
                    u.color = 'black'
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self._right_rotate(k)
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self._left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == 'red':
                    u.color = 'black'
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self._left_rotate(k)
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self._right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 'black'

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node == self.TNULL:
            return 0
        else:
            left_height = self._height(node.left)
            right_height = self._height(node.right)
            return max(left_height, right_height) + 1

def generate_data():
    sizes = []
    heights = []
    for size in range(100, 5001, 100):
        rb_tree = RedBlackTree()
        for elem in range(1, size + 1):
            rb_tree.insert(elem)
        sizes.append(size)
        heights.append(rb_tree.height())
    return sizes, heights

sizes, heights = generate_data()
log_sizes = np.log(sizes)
coefficients = np.polyfit(log_sizes, heights, 1)
regression_line = coefficients[0] * log_sizes + coefficients[1]
theoretical_heights = [2 * np.log2(size + 1) for size in sizes]
plt.scatter(sizes, heights, label='Height of Red-Black Tree', color='blue')
plt.plot(sizes, regression_line, color='red', label=f'Logarithmic Regression')
plt.plot(sizes, theoretical_heights, color='green', label='Theoretical Estimate: Height = 2 * log2(Size + 1)')
plt.xlabel('Number of Elements')
plt.ylabel('Height of Red-Black Tree')
plt.title('Height of Red-Black Tree vs Number of Elements')
plt.legend()
plt.grid(True)
plt.show()

print(f"Формула регрессии: y = {coefficients[0]:.2f} * log(n) + {coefficients[1]:.2f}")
