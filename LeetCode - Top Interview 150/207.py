# 207. Course Schedule
# https://leetcode.com/problems/course-schedule/


from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[0 for _ in range(numCourses)] for _ in range(numCourses)]

        for class_relation in prerequisites:
            course, pre = class_relation

            graph[course][pre] = 1

        def is_there_a_cycle(graph, current, route: List[int]):
            print("is_there_a_cycle", current, route)

            x, y = current

            graph[x][y] = 2

            if y in route:
                return True

            for mid in range(numCourses):
                if graph[y][mid] != 1:
                    continue

                current_route = route[:]
                current_route.append(y)

                mid_result = is_there_a_cycle(graph, (y, mid), current_route)

                if mid_result:
                    return True

            return False

        for i in range(numCourses):
            for j in range(numCourses):
                if graph[i][j] != 1:
                    continue

                if is_there_a_cycle(graph, (i, j), [i]):
                    return False

        return True
