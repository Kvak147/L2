import random
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

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node

        if key < node.val:
            node.left = self._delete(node.left, key)
        elif key > node.val:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            temp = self._minValueNode(node.right)
            node.val = temp.val
            node.right = self._delete(node.right, temp.val)

        return node

    def _minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.val == key:
            return node
        if key < node.val:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.val)
            self._inorder_traversal(node.right, result)

    def preorder_traversal(self):
        result = []
        self._preorder_traversal(self.root, result)
        return result

    def _preorder_traversal(self, node, result):
        if node:
            result.append(node.val)
            self._preorder_traversal(node.left, result)
            self._preorder_traversal(node.right, result)

    def postorder_traversal(self):
        result = []
        self._postorder_traversal(self.root, result)
        return result

    def _postorder_traversal(self, node, result):
        if node:
            self._postorder_traversal(node.left, result)
            self._postorder_traversal(node.right, result)
            result.append(node.val)

    def bfs_traversal(self):
        result = []
        if self.root is None:
            return result

        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result

bst = BinarySearchTree()
num_elements = random.randint(5, 50)
random_elements = random.sample(range(1, 50), num_elements)
for elem in random_elements:
    bst.insert(elem)

def insert_element():
    key = int(input("Введите значение для вставки: "))
    bst.insert(key)
    print(f"Значение {key} вставлено.")

def delete_element():
    key = int(input("Введите значение для удаления: "))
    bst.delete(key)
    print(f"Значение {key} удалено.")

def search_element():
    key = int(input("Введите значение для поиска: "))
    result = bst.search(key)
    if result:
        print(f"Значение {key} найдено.")
    else:
        print(f"Значение {key} не найдено.")

def display_elements():
    print("Элементы дерева (inorder):", bst.inorder_traversal())
    print("Элементы дерева (preorder):", bst.preorder_traversal())
    print("Элементы дерева (postorder):", bst.postorder_traversal())
    print("Элементы дерева (bfs):", bst.bfs_traversal())

while True:
    print("\nМеню:")
    print("1. Вставить элемент")
    print("2. Удалить элемент")
    print("3. Найти элемент")
    print("4. Вывести элементы")
    print("5. Выйти")
    choice = input("Выберите действие: ")

    if choice == '1':
        insert_element()
    elif choice == '2':
        delete_element()
    elif choice == '3':
        search_element()
    elif choice == '4':
        display_elements()
    elif choice == '5':
        break
    else:
        print("Неверный выбор. Пожалуйста, попробуйте снова.")
