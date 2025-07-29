// 452. Minimum Number of Arrows to Burst Balloons
// https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

/**
 * @param {number[][]} points
 * @return {number}
 */
var findMinArrowShots = function (points) {
  const sortedPoints = points.sort((a, b) => a[0] - b[0]);

  let result = 0;
  let currentRange = [...sortedPoints[0]];
  for (let i = 1; i < sortedPoints.length; i++) {
    if (sortedPoints[i][0] <= currentRange[1]) {
      currentRange[0] = Math.max(currentRange[0], sortedPoints[i][0]);
      currentRange[1] = Math.min(currentRange[1], sortedPoints[i][1]);
    } else {
      result += 1;
      currentRange = [...sortedPoints[i]];
    }
  }

  result += 1;

  return result;
};

/*
points = [[10,16],[2,8],[1,6],[7,12]]
sorted = [[1,6],[2,8],[7,12],[10,16]]
                       ^
current = [2,6]
*/
