import matplotlib.pyplot as plt
import numpy as np
from collections import deque

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return TreeNode(key)
        elif key < node.val:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)

        if balance > 1 and key < node.left.val:
            return self._right_rotate(node)
        if balance < -1 and key > node.right.val:
            return self._left_rotate(node)
        if balance > 1 and key > node.left.val:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance < -1 and key < node.right.val:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return 0
        else:
            left_height = self._height(node.left)
            right_height = self._height(node.right)
            return max(left_height, right_height) + 1

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

def generate_data():
    sizes = []
    heights = []
    for size in range(100, 5001, 100):
        avl_tree = AVLTree()
        for elem in range(1, size + 1):
            avl_tree.insert(elem)
        sizes.append(size)
        heights.append(avl_tree.height())
    return sizes, heights

sizes, heights = generate_data()
log_sizes = np.log(sizes)
coefficients = np.polyfit(log_sizes, heights, 1)
regression_line = coefficients[0] * log_sizes + coefficients[1]
theoretical_heights = [1.44 * np.log2(size) for size in sizes]
plt.scatter(sizes, heights, label='Height of AVL Tree', color='blue')
plt.plot(sizes, regression_line, color='red', label='Logarithmic Regression')
plt.plot(sizes, theoretical_heights, color='green', label='Theoretical Estimate: Height = 1.44 * log2(Size)')
plt.xlabel('Number of Elements')
plt.ylabel('Height of AVL Tree')
plt.title('Height of AVL Tree vs Number of Elements')
plt.legend()
plt.grid(True)
plt.show()
print(f"Формула регрессии: y = {coefficients[0]:.2f} * log(n) + {coefficients[1]:.2f}")
