# 138. Copy List with Random Pointer
# https://leetcode.com/problems/copy-list-with-random-pointer/


from typing import Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        hash = {}

        current = head
        while current:
            hash[current] = Node(current.val)

            current = current.next

        current = head
        while current:
            copied = hash[current]
            copied.next = hash.get(current.next)
            copied.random = hash.get(current.random)

            current = current.next

        return hash.get(head)


solution = Solution()

print(solution.copyRandomList(head=[[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]))
print(solution.copyRandomList(head=[[1, 1], [2, 1]]))
print(solution.copyRandomList(head=[[3, None], [3, 0], [3, None]]))
