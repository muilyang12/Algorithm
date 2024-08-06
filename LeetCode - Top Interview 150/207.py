# 207. Course Schedule
# https://leetcode.com/problems/course-schedule/


from typing import List


class Solution:
    def canFinish1(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[0 for _ in range(numCourses)] for _ in range(numCourses)]

        for class_relation in prerequisites:
            course, pre = class_relation

            graph[course][pre] = 1

        def is_there_a_cycle(graph, current, route: List[int]):
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

    def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = [[] for _ in range(numCourses)]

        for class_relation in prerequisites:
            course, pre = class_relation

            pre_map[pre].append(course)

        possible_list = set()

        def has_roop(current, route: List[int]):
            if current in route:
                return True

            new_route = route[:]
            new_route.append(current)

            for next in pre_map[current]:
                if next in possible_list:
                    continue

                if has_roop(next, new_route):
                    return True

            possible_list.add(current)

            return False

        for i in range(numCourses):
            if has_roop(i, []):
                return False

        return True
