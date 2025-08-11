// 207. Course Schedule
// https://leetcode.com/problems/course-schedule/

/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
var canFinish = function (numCourses, prerequisites) {
  const graph = {};
  prerequisites.forEach(([target, prerequisite]) => {
    if (graph[target]) graph[target].push(prerequisite);
    else graph[target] = [prerequisite];
  });

  const noCycleCourses = new Set();

  for (let i = 0; i < numCourses; i++) {
    if (checkCycle(i, graph, noCycleCourses, new Set())) return false;

    noCycleCourses.add(i);
  }

  return true;
};

const checkCycle = (targetCourse, graph, noCycleCourses, visited) => {
  if (visited.has(targetCourse)) return true;
  if (noCycleCourses.has(targetCourse)) return false;

  const prerequisites = graph[targetCourse];

  if (!prerequisites) return false;

  visited.add(targetCourse);
  for (let i = 0; i < prerequisites.length; i++) {
    const isCycle = checkCycle(prerequisites[i], graph, noCycleCourses, visited);

    if (isCycle) return true;
  }
  visited.delete(targetCourse);

  return false;
};
