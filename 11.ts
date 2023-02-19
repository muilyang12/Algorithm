// 11. Container With Most Water
// https://leetcode.com/problems/container-with-most-water/

// Brute Force
// time complexity: O(n^2) || space complexity: O(1)
function maxArea1(height: number[]): number {
  let result = 0;

  for (let i = 0; i < height.length; i++) {
    for (let j = i + 1; j < height.length; j++) {
      const volume = (j - i) * Math.min(height[i], height[j]);

      result = volume > result ? volume : result;
    }
  }

  return result;
}

// Two Pointer
function maxArea2(height: number[]): number {
  let result = 0;
  let left = 0;
  let right = height.length - 1;

  while (left < right) {
    const volume = (right - left) * Math.min(height[left], height[right]);
    result = Math.max(result, volume);

    if (height[left] < height[right]) {
      left += 1;
    } else {
      right -= 1;
    }
  }

  return result;
}
