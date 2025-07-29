// 57. Insert Interval
// https://leetcode.com/problems/insert-interval/

/**
 * @param {number[][]} intervals
 * @param {number[]} newInterval
 * @return {number[][]}
 */
var insert = function (intervals, newInterval) {
  const result = [];

  let i;
  const mergedInterval = [...newInterval];
  for (i = 0; i < intervals.length; i++) {
    if (intervals[i][1] < mergedInterval[0]) {
      result.push(intervals[i]);

      continue;
    }

    if (mergedInterval[1] >= intervals[i][0]) {
      mergedInterval[0] = Math.min(mergedInterval[0], intervals[i][0]);
      mergedInterval[1] = Math.max(mergedInterval[1], intervals[i][1]);
    } else {
      break;
    }
  }

  result.push(mergedInterval);
  result.push(...intervals.slice(i));

  return result;
};

/*
intervals = [[1,3],[6,9]]
newInterval = [2,5]

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
                                       ^
newInterval = [4,8]
mergedInterval = [3,10]
*/
