// 53. Maximum Subarray
// https://leetcode.com/problems/maximum-subarray/

// Brute Force
// time complexity: O(n^3) || space complexity: O(1)
function maxSubArray1(nums: number[]): number {
  let result = nums[0];

  for (let i = 0; i < nums.length; i++) {
    for (let j = i; j < nums.length; j++) {
      let value = 0;

      for (let k = i; k <= j; k++) {
        value += nums[k];
      }

      result = Math.max(result, value);
    }
  }

  return result;
}

// time complexity: O(n^2) || space complexity: O(1)
function maxSubArray2(nums: number[]): number {
  let result = nums[0];

  for (let i = 0; i < nums.length; i++) {
    let tempTotal = 0;

    for (let j = i; j < nums.length; j++) {
      tempTotal += nums[j];

      result = Math.max(result, tempTotal);
    }
  }

  return result;
}

// Dynamic Programming
// time complexity: O(2n) = O(n) || space complexity: O(n)
function maxSubArray3(nums: number[]): number {
  const dp: number[] = [];
  dp[0] = nums[0];

  for (let i = 1; i < nums.length; i++) {
    dp[i] = Math.max(dp[i - 1] + nums[i], nums[i]);
  }

  const result = Math.max(...dp);

  return result;
}

// Dynamic Programming
// time complexity: O(n) || space complexity: O(1)
function maxSubArray4(nums: number[]): number {
  let dpVariable = nums[0];
  let result = nums[0];

  for (let i = 1; i < nums.length; i++) {
    dpVariable = Math.max(dpVariable + nums[i], nums[i]);
    result = Math.max(result, dpVariable);
  }

  return result;
}
