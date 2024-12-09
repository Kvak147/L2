import random
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

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if not node:
            return node
        elif key < node.val:
            node.left = self._delete(node.left, key)
        elif key > node.val:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._get_min_value_node(node.right)
            node.val = temp.val
            node.right = self._delete(node.right, temp.val)

        if node is None:
            return node

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)

        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._right_rotate(node)
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._left_rotate(node)
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

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

    def level_order_traversal(self):
        result = []
        if not self.root:
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

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _get_min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

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

# Создаем дерево и добавляем случайные элементы
avl_tree = AVLTree()
num_elements = random.randint(10, 50)
random_elements = random.sample(range(1, 100), num_elements)
for elem in random_elements:
    avl_tree.insert(elem)

# Функции для взаимодействия с пользователем
def insert_element():
    key = int(input("Введите значение для вставки: "))
    avl_tree.insert(key)
    print(f"Значение {key} вставлено.")

def delete_element():
    key = int(input("Введите значение для удаления: "))
    avl_tree.delete(key)
    print(f"Значение {key} удалено.")

def search_element():
    key = int(input("Введите значение для поиска: "))
    result = avl_tree.search(key)
    if result:
        print(f"Значение {key} найдено.")
    else:
        print(f"Значение {key} не найдено.")

def display_elements():
    print("Элементы дерева (inorder):", avl_tree.inorder_traversal())
    print("Элементы дерева (preorder):", avl_tree.preorder_traversal())
    print("Элементы дерева (postorder):", avl_tree.postorder_traversal())
    print("Элементы дерева (level-order):", avl_tree.level_order_traversal())

# Основной цикл программы
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
