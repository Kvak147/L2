import random
import matplotlib.pyplot as plt
import numpy as np
from collections import deque

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return 0
        else:
            left_height = self._height(node.left)
            right_height = self._height(node.right)
            return max(left_height, right_height) + 1

def generate_data(num_trials=10):
    sizes = []
    heights = []
    for size in range(100, 5001, 100):
        heights_list = []
        for _ in range(num_trials):
            bst = BinarySearchTree()
            random_elements = random.sample(range(1, 10000), size)
            for elem in random_elements:
                bst.insert(elem)
            heights_list.append(bst.height())
        median_height = int(np.median(heights_list))
        sizes.append(size)
        heights.append(median_height)
    return sizes, heights

sizes, heights = generate_data()
log_sizes = np.log(sizes)
coefficients = np.polyfit(log_sizes, heights, 1)
regression_line = coefficients[0] * log_sizes + coefficients[1]
plt.scatter(sizes, heights, label='Height of BST', color='blue')
plt.plot(sizes, regression_line, color='red', label='Logarithmic Regression')
plt.xlabel('Number of Elements')
plt.ylabel('Height of BST')
plt.title('Height of BST vs Number of Elements')
plt.legend()
plt.grid(True)
plt.show()

print(f"Формула регрессии: y = {coefficients[0]:.2f} * log(n) + {coefficients[1]:.2f}")
