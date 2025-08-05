// 540. Single Element in a Sorted Array
// https://leetcode.com/problems/single-element-in-a-sorted-array/

/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNonDuplicate = function (nums) {
  let left = 0;
  let right = nums.length - 1;

  while (left <= right) {
    let mid = Math.floor((left + right) / 2);

    console.log(left, mid, right);

    if (mid % 2 === 0) {
      if (nums[mid] === nums[mid + 1]) left = mid + 1;
      else if (nums[mid] !== nums[mid + 1] && nums[mid] !== nums[mid - 1]) return nums[mid];
      else right = mid - 1;
    } else {
      if (nums[mid] === nums[mid - 1]) left = mid + 1;
      else if (nums[mid] !== nums[mid - 1] && nums[mid] !== nums[mid + 1]) return nums[mid];
      else right = mid - 1;
    }
  }
};

/*
nums = [1,1,2,3,3,4,4,8,8]
        ^ ^   ^

nums = [3,3,7,7,10,11,11]
        ^     ^       ^
*/
