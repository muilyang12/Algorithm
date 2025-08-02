// 120. Triangle
// https://leetcode.com/problems/triangle/

/**
 * @param {number[][]} triangle
 * @return {number}
 */
var minimumTotal = function (triangle) {
  const memo = [];
  for (let i = 0; i < triangle.length; i++) {
    memo.push([]);

    for (let j = 0; j < triangle[i].length; j++) {
      memo[i].push(triangle[i][j]);
    }
  }

  for (let i = 1; i < triangle.length; i++) {
    for (let j = 0; j < triangle[i].length; j++) {
      const upperLeft = memo[i - 1][j - 1] ?? Number.POSITIVE_INFINITY;
      const upperRight = memo[i - 1][j] ?? Number.POSITIVE_INFINITY;

      memo[i][j] = Math.min(upperLeft, upperRight) + memo[i][j];
    }
  }

  let result = Number.POSITIVE_INFINITY;
  for (let num of memo[memo.length - 1]) {
    result = Math.min(result, num);
  }

  return result;
};
