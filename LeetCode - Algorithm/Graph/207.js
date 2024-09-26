// 207. Course Schedule
// https://leetcode.com/problems/course-schedule/

/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */

// Time Limit Exceeded :(
var canFinish1 = function (numCourses, prerequisites) {
  const coursesMap = {};
  prerequisites.forEach(([course, prerequisite]) => {
    if (!coursesMap[course]) coursesMap[course] = [];

    coursesMap[course].push(prerequisite);
  });

  const isThereLoop = (course, visited) => {
    if (visited.includes(course)) return true;

    const targetCourses = coursesMap[course];
    if (!targetCourses) return false;

    visited.push(course);

    let result = false;

    for (let i = 0; i < targetCourses.length; i++) {
      result = result || isThereLoop(targetCourses[i], visited);
      if (result) return result;
    }

    visited.pop();

    return result;
  };

  for (let i = 0; i < numCourses; i++) {
    if (isThereLoop(i, [])) return false;
  }

  return true;
};

var canFinish2 = function (numCourses, prerequisites) {
  const coursesMap = {};
  prerequisites.forEach(([course, prerequisite]) => {
    if (!coursesMap[course]) coursesMap[course] = [];

    coursesMap[course].push(prerequisite);
  });

  const okaySet = new Set();

  const isThereLoop = (course, visited) => {
    if (visited.includes(course)) return true;
    if (okaySet.has(course)) return false;

    const targetCourses = coursesMap[course];
    if (!targetCourses) return false;

    visited.push(course);

    let result = false;

    for (let i = 0; i < targetCourses.length; i++) {
      result = result || isThereLoop(targetCourses[i], visited);
      if (result) return result;
    }

    visited.pop();

    okaySet.add(course);

    return result;
  };

  for (let i = 0; i < numCourses; i++) {
    if (isThereLoop(i, [])) return false;
  }

  return true;
};

`
0 -> [1]
1 -> [0]

0 -> [1, 2]
1 -> [2, 3]
2 -> [3]

0 -> [5]
1 -> [0, 7]
2 -> [6]
6 -> [4]
7 -> [0]
`;
