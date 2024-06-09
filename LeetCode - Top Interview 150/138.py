# 138. Copy List with Random Pointer
# https://leetcode.com/problems/copy-list-with-random-pointer/


from typing import Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    # time complexity: O(2n) = O(n)
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
            # hash[current.next]와 달리 hash.get(current.next)를 통해 값을 가져올 경우 KeyError가
            # 발생하지 않고, None이 리턴되게 됩니다.

            current = current.next

        return hash.get(head)


solution = Solution()

print(solution.copyRandomList(head=[[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]))
print(solution.copyRandomList(head=[[1, 1], [2, 1]]))
print(solution.copyRandomList(head=[[3, None], [3, 0], [3, None]]))
