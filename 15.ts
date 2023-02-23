// 15. 3Sum
// https://leetcode.com/problems/3sum/

// Brute Force
// time complexity: O(n^3) || space complexity: O(1)
function threeSum1(nums: number[]): number[][] {
  const result: number[][] = [];
  const added = new Set();

  const length = nums.length;
  for (let i = 0; i < length - 2; i++) {
    for (let j = i + 1; j < length - 1; j++) {
      for (let k = j + 1; k < length; k++) {
        if (nums[i] + nums[j] + nums[k] === 0) {
          const answer = [nums[i], nums[j], nums[k]].sort((a, b) => a - b);
        
          if (!added.has(answer.join(""))) {
            result.push(answer);
            added.add(answer.join(""));
          }
        }
      }
    }
  }

  return result;
}

function threeSum2(nums: number[]): number[][] {
  const result: number[][] = [];
  const added = new Set();

  const length = nums.length;
  for (let i = 0; i < length - 2; i++) {
    const history = new Set();

    for (let j = i + 1; j < length - 1; j++) {
      const complement = 0 - (nums[i] + nums[j]);

      if (history.has(complement)) {
        const answer = [nums[i], complement, nums[j]];

        if (!added.has(answer.join(""))) {
          result.push(answer);
          added.add(answer.join(""));
        }
      } else {
        history.add(nums[j]);
      }
    }
  }

  return result;
}
        
