from typing import List, Any, Dict, Set, Generator


class StaticArray:
    def __init__(self, capacity: int):
        """
        Initialize a static array of a given capacity.
        """
        self.capacity = capacity
        self.array = [None] * capacity

    def set(self, index: int, value: int) -> None:
        """
        Set the value at a particular index.
        """
        if 0 <= index < self.capacity:
            self.array[index] = value
        else:
            raise IndexError("Index out of bounds")

    def get(self, index: int) -> int:
        """
        Retrieve the value at a particular index.
        """
        if 0 <= index < self.capacity:
            return self.array[index]
        else:
            raise IndexError("Index out of bounds")


class DynamicArray:
    def __init__(self):
        """
        Initialize an empty dynamic array.
        """
        self.array = []

    def append(self, value: int) -> None:
        """
        Add a value to the end of the dynamic array.
        """
        self.array.append(value)

    def insert(self, index: int, value: int) -> None:
        """
        Insert a value at a particular index.
        """
        self.array.insert(index, value)

    def delete(self, index: int) -> None:
        """
        Delete the value at a particular index.
        """
        if 0 <= index < len(self.array):
            self.array.pop(index)
        else:
            raise IndexError("Index out of bounds")

    def get(self, index: int) -> int:
        """
        Retrieve the value at a particular index.
        """
        if 0 <= index < len(self.array):
            return self.array[index]
        else:
            raise IndexError("Index out of bounds")


class Node:
    def __init__(self, value: int):
        """
        Initialize a node.
        """
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        """
        Initialize an empty singly linked list.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, value: int) -> None:
        """
        Add a node with a value to the end of the linked list.
        """
        new_node = Node(value)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
        self.size += 1

    def insert(self, position: int, value: int) -> None:
        """
        Insert a node with a value at a particular position.
        """
        if position < 0 or position > self.size:
            raise IndexError("Index out of bounds")

        new_node = Node(value)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            if not self.tail:
                self.tail = new_node
        else:
            current = self.head
            for _ in range(position - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            if new_node.next is None:
                self.tail = new_node
        self.size += 1

    def delete(self, value: int) -> None:
        """
        Delete the first node with a specific value.
        """
        current = self.head
        prev = None
        while current:
            if current.value == value:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                if current == self.tail:
                    self.tail = prev
                self.size -= 1
                return
            prev = current
            current = current.next

    def find(self, value: int) -> Node:
        """
        Find a node with a specific value.
        """
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def size(self) -> int:
        """
        Returns the number of elements in the linked list.
        """
        return self.size

    def is_empty(self) -> bool:
        """
        Checks if the linked list is empty.
        """
        return self.size == 0

    def print_list(self) -> None:
        """
        Prints all elements in the linked list.
        """
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def reverse(self) -> None:
        """
        Reverse the linked list in-place.
        """
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def get_head(self) -> Node:
        """
        Returns the head node of the linked list.
        """
        return self.head

    def get_tail(self) -> Node:
        """
        Returns the tail node of the linked list.
        """
        return self.tail


class DoubleNode:
    def __init__(self, value: int, next_node=None, prev_node=None):
        """
        Initialize a double node with value, next, and previous.
        """
        self.value = value
        self.next = next_node
        self.prev = prev_node


class DoublyLinkedList:
    def __init__(self):
        """
        Initialize an empty doubly linked list.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, value: int) -> None:
        """
        Add a node with a value to the end of the linked list.
        """
        new_node = DoubleNode(value)
        if self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
        else:
            self.head = new_node
        self.tail = new_node
        self.size += 1

    def insert(self, position: int, value: int) -> None:
        """
        Insert a node with a value at a particular position.
        """
        if position < 0 or position > self.size:
            raise IndexError("Index out of bounds")

        new_node = DoubleNode(value)
        if position == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            if not self.tail:
                self.tail = new_node
        else:
            current = self.head
            for _ in range(position - 1):
                current = current.next
            new_node.next = current.next
            if current.next:
                current.next.prev = new_node
            current.next = new_node
            new_node.prev = current
            if new_node.next is None:
                self.tail = new_node
        self.size += 1

    def delete(self, value: int) -> None:
        """
        Delete the first node with a specific value.
        """
        current = self.head
        while current:
            if current.value == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                self.size -= 1
                return
            current = current.next

    def find(self, value: int) -> DoubleNode:
        """
        Find a node with a specific value.
        """
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def size(self) -> int:
        """
        Returns the number of elements in the linked list.
        """
        return self.size

    def is_empty(self) -> bool:
        """
        Checks if the linked list is empty.
        """
        return self.size == 0

    def print_list(self) -> None:
        """
        Prints all elements in the linked list.
        """
        current = self.head
        while current:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")

    def reverse(self) -> None:
        """
        Reverse the linked list in-place.
        """
        current = self.head
        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev
        self.head, self.tail = self.tail, self.head

    def get_head(self) -> DoubleNode:
        """
        Returns the head node of the linked list.
        """
        return self.head

    def get_tail(self) -> DoubleNode:
        """
        Returns the tail node of the linked list.
        """
        return self.tail


class Queue:
    def __init__(self):
        """
        Initialize an empty queue.
        """
        self.queue = []

    def enqueue(self, value: int) -> None:
        """
        Add a value to the end of the queue.
        """
        self.queue.append(value)

    def dequeue(self) -> int:
        """
        Remove a value from the front of the queue and return it.
        """
        if self.queue:
            return self.queue.pop(0)
        else:
            raise IndexError("Dequeue from empty queue")

    def peek(self) -> int:
        """
        Peek at the value at the front of the queue without removing it.
        """
        if self.queue:
            return self.queue[0]
        else:
            raise IndexError("Peek from empty queue")

    def is_empty(self) -> bool:
        """
        Check if the queue is empty.
        """
        return len(self.queue) == 0


class TreeNode:
    def __init__(self, value: int):
        """
        Initialize a tree node with value.
        """
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        """
        Initialize an empty binary search tree.
        """
        self.root = None

    def insert(self, value: int) -> None:
        """
        Insert a node with a specific value into the binary search tree.
        """

        def _insert(root, value):
            if root is None:
                return TreeNode(value)
            if value < root.value:
                root.left = _insert(root.left, value)
            else:
                root.right = _insert(root.right, value)
            return root

        self.root = _insert(self.root, value)

    def delete(self, value: int) -> None:
        """
        Remove a node with a specific value from the binary search tree.
        """

        def _delete(root, value):
            if root is None:
                return root
            if value < root.value:
                root.left = _delete(root.left, value)
            elif value > root.value:
                root.right = _delete(root.right, value)
            else:
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                min_node = self._find_min(root.right)
                root.value = min_node.value
                root.right = _delete(root.right, min_node.value)
            return root

        self.root = _delete(self.root, value)

    def search(self, value: int) -> TreeNode:
        """
        Search for a node with a specific value in the binary search tree.
        """

        def _search(root, value):
            if root is None or root.value == value:
                return root
            if value < root.value:
                return _search(root.left, value)
            return _search(root.right, value)

        return _search(self.root, value)

    def inorder_traversal(self) -> List[int]:
        """
        Perform an in-order traversal of the binary search tree.
        """

        def _inorder(root):
            return (
                _inorder(root.left) + [root.value] + _inorder(root.right)
                if root
                else []
            )

        return _inorder(self.root)

    def size(self) -> int:
        """
        Returns the number of nodes in the tree.
        """

        def _size(root):
            return 0 if root is None else 1 + _size(root.left) + _size(root.right)

        return _size(self.root)

    def is_empty(self) -> bool:
        """
        Checks if the tree is empty.
        """
        return self.root is None

    def height(self) -> int:
        """
        Returns the height of the tree.
        """

        def _height(root):
            if root is None:
                return -1
            left_height = _height(root.left)
            right_height = _height(root.right)
            return max(left_height, right_height) + 1

        return _height(self.root)

    def preorder_traversal(self) -> List[int]:
        """
        Perform a pre-order traversal of the binary search tree.
        """

        def _preorder(root):
            return (
                [root.value] + _preorder(root.left) + _preorder(root.right)
                if root
                else []
            )

        return _preorder(self.root)

    def postorder_traversal(self) -> List[int]:
        """
        Perform a post-order traversal of the binary search tree.
        """

        def _postorder(root):
            return (
                _postorder(root.left) + _postorder(root.right) + [root.value]
                if root
                else []
            )

        return _postorder(self.root)

    def _find_min(self, root: TreeNode) -> TreeNode:
        """
        Find the node with the minimum value in a binary search tree.
        """
        while root.left:
            root = root.left
        return root
