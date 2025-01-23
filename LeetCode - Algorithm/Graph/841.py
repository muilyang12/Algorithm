# 841. Keys and Rooms
# https://leetcode.com/problems/keys-and-rooms/


from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        result = False

        def dfs(currentRoom: int, visited: set):
            nonlocal result

            if len(visited) == len(rooms):
                result = True

            for room in rooms[currentRoom]:
                if room in visited:
                    continue

                visited.add(room)
                dfs(room, visited)

        dfs(0, set([0]))

        return result
