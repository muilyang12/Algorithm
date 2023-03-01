// 198. House Robber
// https://leetcode.com/problems/house-robber/

// Dynamic Programming
// time complexity: O(n) || space complexity: O(n)
function rob1(nums: number[]): number {
  if (nums.length < 2) return nums[0];

  const dp: number[] = [];

  dp[0] = nums[0];
  dp[1] = Math.max(dp[0], nums[1]);

  for (let i = 2; i < nums.length; i++) {
    dp[i] = Math.max(dp[i - 2] + nums[i], dp[i - 1]);
  }

  return dp[nums.length - 1];
}

// Dynamic Programming
// time complexity: O(n) || space complexity: O(2) = O(1)
function rob2(nums: number[]): number {
  if (nums.length < 2) return nums[0];

  let minusTwo = nums[0];
  let minusOne = Math.max(minusTwo, nums[1]);

  for (let i = 2; i < nums.length; i++) {
    const temp = minusOne;

    minusOne = Math.max(minusTwo + nums[i], minusOne);
    minusTwo = temp;
  }

  return minusOne;
}

// Divide and conquer
// time complexity: O(n^2) || space complexity: O(n) => Depth of stack
function rob3(nums: number[]): number {
  if (nums.length < 1) return 0;
  else if (nums.length === 1) return nums[0];

  return Math.max(nums[0] + rob3(nums.slice(2)), rob3(nums.slice(1)));
}
