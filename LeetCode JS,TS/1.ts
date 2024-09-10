// 1. Two Sum
// https://leetcode.com/problems/two-sum/

// Brute Force
// time complexity: O(n^2) || space complexity: O(1)
function twoSum1(nums: number[], target: number): number[] {
  for (let i: number = 0; i < nums.length; i++) {
    for (let j: number = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] === target) return [i, j];
    }
  }

  return [];
}

// Hash Table
// time complexity: O(2n) = O(n) || space complexity: O(n)
function twoSum2(nums: number[], target: number): number[] {
  const hashTable = {};
  nums.forEach((num, index) => {
    hashTable[num] = index;
  });

  for (let i = 0; i < nums.length; i++) {
    const targetNum = target - nums[i];
    if (hashTable.hasOwnProperty(targetNum) && i !== hashTable[targetNum]) {
      return [i, hashTable[targetNum]];
    }
  }

  return [];
}

// Hash Table
// time complexity: O(n) || space complexity: O(n)
function twoSum3(nums: number[], target: number): number[] {
  const hashTable = {};
  for (let i = 0; i < nums.length; i++) {
    const targetNum: number = target - nums[i];

    if (hashTable.hasOwnProperty(targetNum)) return [hashTable[targetNum], i];

    hashTable[nums[i]] = i;
  }

  return [];
}
