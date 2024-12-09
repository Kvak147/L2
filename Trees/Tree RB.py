import random
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

    def delete(self, key):
        z = self.TNULL
        node = self.root
        while node != self.TNULL:
            if node.val == key:
                z = node

            if node.val <= key:
                node = node.right
            else:
                node = node.left

        if z == self.TNULL:
            print(f"Key {key} not found in the tree")
            return

        y = z
        y_original_color = y.color
        if z.left == self.TNULL:
            x = z.right
            self._transplant(z, z.right)
        elif z.right == self.TNULL:
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self._minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 'black':
            self._fix_delete(x)

    def _transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _minimum(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node

    def _fix_delete(self, x):
        while x != self.root and x.color == 'black':
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self._left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == 'black' and w.right.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.right.color == 'black':
                        w.left.color = 'black'
                        w.color = 'red'
                        self._right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.right.color = 'black'
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self._right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == 'black' and w.left.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.left.color == 'black':
                        w.right.color = 'black'
                        w.color = 'red'
                        self._left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.left.color = 'black'
                    self._right_rotate(x.parent)
                    x = self.root
        x.color = 'black'

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        while node != self.TNULL and key != node.val:
            if key < node.val:
                node = node.left
            else:
                node = node.right
        return node

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        if node != self.TNULL:
            self._inorder_traversal(node.left, result)
            result.append(node.val)
            self._inorder_traversal(node.right, result)

    def preorder_traversal(self):
        result = []
        self._preorder_traversal(self.root, result)
        return result

    def _preorder_traversal(self, node, result):
        if node != self.TNULL:
            result.append(node.val)
            self._preorder_traversal(node.left, result)
            self._preorder_traversal(node.right, result)

    def postorder_traversal(self):
        result = []
        self._postorder_traversal(self.root, result)
        return result

    def _postorder_traversal(self, node, result):
        if node != self.TNULL:
            self._postorder_traversal(node.left, result)
            self._postorder_traversal(node.right, result)
            result.append(node.val)

    def level_order_traversal(self):
        result = []
        if self.root == self.TNULL:
            return result
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            result.append(node.val)
            if node.left != self.TNULL:
                queue.append(node.left)
            if node.right != self.TNULL:
                queue.append(node.right)
        return result

rb_tree = RedBlackTree()
num_elements = random.randint(10, 50)
random_elements = random.sample(range(1, 100), num_elements)
for elem in random_elements:
    rb_tree.insert(elem)

def insert_element():
    key = int(input("Введите значение для вставки: "))
    rb_tree.insert(key)
    print(f"Значение {key} вставлено.")

def delete_element():
    key = int(input("Введите значение для удаления: "))
    rb_tree.delete(key)
    print(f"Значение {key} удалено.")

def search_element():
    key = int(input("Введите значение для поиска: "))
    result = rb_tree.search(key)
    if result != rb_tree.TNULL:
        print(f"Значение {key} найдено.")
    else:
        print(f"Значение {key} не найдено.")

def display_elements():
    print("Элементы дерева (inorder):", rb_tree.inorder_traversal())
    print("Элементы дерева (preorder):", rb_tree.preorder_traversal())
    print("Элементы дерева (postorder):", rb_tree.postorder_traversal())
    print("Элементы дерева (level-order):", rb_tree.level_order_traversal())

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
