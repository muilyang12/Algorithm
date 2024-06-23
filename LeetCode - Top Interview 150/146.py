# 146. LRU Cache
# https://leetcode.com/problems/lru-cache/


class LRUCache1:
    def __init__(self, capacity: int):
        self.cache = {}
        self.inserted_sequence = []
        self.capacity = capacity

    # time complexity: O(n)
    def get(self, key: int) -> int:
        if key in self.cache:
            self.inserted_sequence.remove(key)
            self.inserted_sequence.append(key)

            return self.cache[key]

        return -1

    # time complexity: O(n)
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.inserted_sequence.remove(key)

        self.cache[key] = value
        self.inserted_sequence.append(key)

        if len(self.inserted_sequence) > self.capacity:
            target_key = self.inserted_sequence.pop(0)
            del self.cache[target_key]


class LRUCache2:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity

        self.head = self.Node("head", -1)
        self.tail = self.Node("tail", -1)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.cache = {}

    # time complexity: O(1)
    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1

        target_node = self.cache[key]
        target_key = target_node.key
        target_value = target_node.value

        self.remove_node(target_key)
        self.append_node(target_key, target_value)

        return target_value

    # time complexity: O(1)
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove_node(key)

        self.append_node(key, value)

        if len(self.cache) > self.capacity:
            first_node = self.head.next
            self.remove_node(first_node.key)

    def append_node(self, key, value):
        new_node = self.Node(key, value)

        last_node = self.tail.prev

        last_node.next = new_node
        new_node.next = self.tail
        new_node.prev = last_node
        self.tail.prev = new_node

        self.cache[key] = new_node

    def remove_node(self, key):
        target_node = self.cache[key]

        prev_node = target_node.prev
        next_node = target_node.next

        prev_node.next = next_node
        next_node.prev = prev_node

        del self.cache[key]
