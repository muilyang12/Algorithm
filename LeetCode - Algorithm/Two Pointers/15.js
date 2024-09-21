// 15. 3Sum
// https://leetcode.com/problems/3sum/

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
  resultSet = new Set();

  sortedNums = nums.sort((a, b) => a - b);

  for (i = 0; i < nums.length - 2; i++) {
    if (nums[i] > 0) {
      break;
    }

    left = i + 1;
    right = nums.length - 1;

    while (left < right) {
      complement = -nums[i];

      if (nums[left] + nums[right] === complement) {
        resultSet.add(`${nums[i]}/${nums[left]}/${nums[right]}`);
        left += 1;
        right -= 1;
      } else if (nums[left] + nums[right] < complement) {
        left += 1;
      } else {
        right -= 1;
      }
    }
  }

  result = Array.from(resultSet).map((value) => value.split("/").map((elem) => Number(elem)));

  return result;
};

`
If the array is sorted, we can find two elements that make a certain sum using the two-pointer method, 
starting left pointer at the beginning and the right one at the end of the array.

In JavaScript, when using Array.prototype.sort(), it's important to provide a compare function (compareFn).
Without a proper compareFn, the array elements are sorted as strings by default. This can cause issues
with negative numbers, leading to incorrect sorting.  For example, [-5, -4, -3, -2, -1] will be sorted
as [-1, -2, -3, -4, -5] if no compareFn is provided.
`;
