# 146. LRU Cache
# https://leetcode.com/problems/lru-cache/

from typing import Dict


class LRUCache:
    class Node:
        def __init__(self, key: int, value: int):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.first: self.Node = None
        self.last: self.Node = None
        self.cache: Dict[int, self.Node] = {}

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1

        value = self.cache[key].value

        self.removeNode(key)

        self.addNode(key, value)

        return value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.removeNode(key)

        self.addNode(key, value)

        if len(self.cache) > self.capacity:
            self.removeNode(self.last.key)

    def addNode(self, key, value):
        newNode = self.Node(key, value)

        if self.first:
            newNode.next = self.first
            self.first.prev = newNode
            self.first = newNode
        else:
            self.first = newNode
            self.last = newNode

        self.cache[key] = newNode

    def removeNode(self, key):
        targetNode = self.cache[key]

        prev = targetNode.prev
        next = targetNode.next

        # If it is the last node.
        if not next:
            self.last = prev

        # If it is the first node.
        if not prev:
            self.first = self.first.next

        # If it is in the middle of the List
        if next and prev:
            prev.next = next

        del self.cache[key]
