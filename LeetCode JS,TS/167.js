// 167. Two Sum II - Input Array Is Sorted
// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */

// Sorted Array -> Binary Search
// time complexity: O(nlogn) || space complexity: O(1)
var twoSum1 = function (numbers, target) {
  for (let i = 0; i < numbers.length; i++) {
    const complement = target - numbers[i];
    const complementIndexInSlice = binarySearch(numbers.slice(i + 1), complement);

    if (complementIndexInSlice > -1) {
      const complementIndex = complementIndexInSlice + (i + 1);
      return [i + 1, complementIndex + 1];
    }
  }
};

function binarySearch(numbers, target) {
  let front = 0;
  let rear = numbers.length - 1;

  let mid;
  while (front <= rear) {
    mid = Math.floor((front + rear) / 2);

    if (target > numbers[mid]) {
      front = mid + 1;
    } else if (target < numbers[mid]) {
      rear = mid - 1;
    } else {
      return mid;
    }
  }

  return -1;
}

// Two Pointer
// time complexity: O(n) || space complexity: O(1)
var twoSum2 = function (numbers, target) {
  let front = 0;
  let rear = numbers.length - 1;

  while (front < rear) {
    const currentValue = numbers[front] + numbers[rear];

    if (currentValue < target) {
      front += 1;
    } else if (currentValue > target) {
      rear -= 1;
    } else {
      break;
    }
  }

  return [front + 1, rear + 1];
};
