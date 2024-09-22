// 45. Jump Game II
// https://leetcode.com/problems/jump-game-ii/

/**
 * @param {number[]} nums
 * @return {number}
 */
var jump1 = function (nums) {
  let current = 0;
  let result = 0;

  while (current < nums.length - 1) {
    let targetJump = -1;
    let reachableDistance = -1;

    for (i = 1; i <= nums[current]; i++) {
      if (current + i >= nums.length - 1) {
        targetJump = i;
        break;
      }

      if (i + nums[current + i] > reachableDistance) {
        targetJump = i;
        reachableDistance = i + nums[current + i];
      }
    }

    current += targetJump;
    result += 1;
  }

  return result;
};

var jump2 = function (nums) {
  if (nums.length === 1) return 0;

  result = 0;

  farthestFromCurrentRegion = 0;
  endOfRegion = 0;

  for (let i = 0; i < nums.length; i++) {
    farthestFromCurrentRegion = Math.max(farthestFromCurrentRegion, i + nums[i]);

    if (i === endOfRegion) {
      endOfRegion = farthestFromCurrentRegion;

      result += 1;

      if (endOfRegion >= nums.length - 1) return result;
    }
  }
};

`
nums = [2,3,1,1,4]
                ^
`;
