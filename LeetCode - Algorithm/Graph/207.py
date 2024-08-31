# 207. Course Schedule
# https://leetcode.com/problems/course-schedule/

from typing import List
from collections import defaultdict


class Solution:
    # time complexity: O(n ^ 2)
    # Time Limit Exceeded :(
    # It can be improved by caching and memoization. The process currently rechecks whether a certain course
    # can be taken, even though it was already verified in a previous route, which is very wasteful.
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisiteGraph = defaultdict(list)

        for targetCourse, preCourse in prerequisites:
            prerequisiteGraph[targetCourse].append(preCourse)

        for i in range(numCourses):
            if not self.isPossibleToTake(prerequisiteGraph, i, set()):
                return False

        return True

    # I initially didn't call visited.remove(courseNum). When the task is to check for the presence of a cycle,
    # which means verifying a specific path, 'add' and 'remove' should be called consecutively.
    def isPossibleToTake(
        self,
        prerequisiteGraph: defaultdict[int, List[int]],
        courseNum: int,
        visited: set[int],
    ):
        if courseNum in visited:
            return False

        visited.add(courseNum)

        for course in prerequisiteGraph[courseNum]:
            if not self.isPossibleToTake(prerequisiteGraph, course, visited):
                return False

        visited.remove(courseNum)

        return True
