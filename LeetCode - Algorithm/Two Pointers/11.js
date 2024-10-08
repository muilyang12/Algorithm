// 11. Container With Most Water
// https://leetcode.com/problems/container-with-most-water/

/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
  let left = 0;
  let right = height.length - 1;

  let result = 0;

  while (left < right) {
    const area = (right - left) * Math.min(height[left], height[right]);
    result = Math.max(result, area);

    if (height[left] <= height[right]) left += 1;
    else right -= 1;
  }

  return result;
};
