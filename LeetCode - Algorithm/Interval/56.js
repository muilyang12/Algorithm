// 56. Merge Intervals
// https://leetcode.com/problems/merge-intervals/

/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function (intervals) {
  const sortedIntervals = intervals.sort((a, b) => a[0] - b[0]);

  const result = [];
  result.push(sortedIntervals[0]);

  for (let i = 1; i < sortedIntervals.length; i++) {
    const [_, firstEnd] = result[result.length - 1];
    const [secondStart, secondEnd] = sortedIntervals[i];

    if (secondStart > firstEnd) result.push(sortedIntervals[i]);
    else result[result.length - 1][1] = Math.max(firstEnd, secondEnd);
  }

  return result;
};
