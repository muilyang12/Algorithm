# 146. LRU Cache
# https://leetcode.com/problems/lru-cache/


class LRUCache1:
    def __init__(self, capacity: int):
        self.cache = {}
        self.inserted_sequence = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.inserted_sequence.remove(key)
            self.inserted_sequence.append(key)

            return self.cache[key]

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.inserted_sequence.remove(key)

        self.cache[key] = value
        self.inserted_sequence.append(key)

        if len(self.inserted_sequence) > self.capacity:
            target_key = self.inserted_sequence.pop(0)
            del self.cache[target_key]

