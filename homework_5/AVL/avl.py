"""Задача 3. AVL"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


def height(node):
    return node.height if node else 0


def update(node):
    node.height = 1 + max(height(node.left), height(node.right))


def rotate_right(node):
    root = node.left
    node.left = root.right
    root.right = node
    update(node)
    update(root)
    return root


def rotate_left(node):
    root = node.right
    node.right = root.left
    root.left = node
    update(node)
    update(root)
    return root


def balance(node):
    update(node)
    diff = height(node.left) - height(node.right)  # положительная разница означает перевес слева
    if diff > 1:
        if height(node.left.left) < height(node.left.right):
            node.left = rotate_left(node.left)  # сначала выпрямляем левое поддерево
        return rotate_right(node)
    if diff < -1:
        if height(node.right.right) < height(node.right.left):
            node.right = rotate_right(node.right)  # симметрично справа
        return rotate_left(node)
    return node


class AVL:
    def __init__(self):
        self.root = None

    def search(self, value):
        node = self.root
        while node is not None:
            if value == node.value:
                return node
            node = node.left if value < node.value else node.right
        return None

    def insert(self, value):
        def add(node):
            if node is None:
                return Node(value)
            if value < node.value:
                node.left = add(node.left)
            elif value > node.value:
                node.right = add(node.right)
            else:
                return node
            return balance(node)
        self.root = add(self.root)

    def delete(self, value):
        def remove(node, key):
            if node is None:
                return None
            if key < node.value:
                node.left = remove(node.left, key)
            elif key > node.value:
                node.right = remove(node.right, key)
            else:
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left
                # следующий по величине ключ заменит удаляемый
                successor = node.right
                while successor.left:
                    successor = successor.left
                node.value = successor.value
                node.right = remove(node.right, successor.value)  # убрать старую копию
            return balance(node)
        self.root = remove(self.root, value)


def draw(root):
    """Дерево боком: правое поддерево сверху"""
    lines = []
    def visit(node, prefix, edge):
        if node is None:
            return
        visit(node.right, prefix + "    ", "/ ")
        lines.append(prefix + edge + str(node.value))
        visit(node.left, prefix + "    ", "\\ ")
    visit(root, "", "")
    return lines or ["(пустое дерево)"]


def demo():
    tree = AVL()
    for value in (30, 20, 10, 25, 40, 50):
        tree.insert(value)
        print(f"вставка {value}:")
        print("\n".join(draw(tree.root)))
    for value in (10, 30):
        tree.delete(value)
        print(f"удаление {value}:")
        print("\n".join(draw(tree.root)))
    print(f"поиск 25: {tree.search(25) is not None}")


if __name__ == "__main__":
    demo()
