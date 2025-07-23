// 11. Container With Most Water
// https://leetcode.com/problems/container-with-most-water/

function maxArea(height: number[]): number {
  let left = 0;
  let right = height.length - 1;

  let result = -1;

  while (left < right) {
    result = Math.max(result, (right - left) * Math.min(height[left], height[right]));

    if (height[left] <= height[right]) left += 1;
    else right -= 1;
  }

  return result;
}

// Hmm... Honestly, no matter how many times I solve this problem, it's still kind of surprising that it doesn't matter which one you move first when the two heights are equal.
