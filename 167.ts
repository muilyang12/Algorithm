// 167. Two Sum II - Input Array Is Sorted
// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

// Hash Table
// time complexity: O(n) || space complexity: O(n)
function twoSum1(nums: number[], target: number): number[] {
  const hashTable = {};
  for (let i = 0; i < nums.length; i++) {
    const targetNum: number = target - nums[i];

    if (hashTable.hasOwnProperty(targetNum)) return [hashTable[targetNum], i];

    hashTable[nums[i]] = i;
  }

  return [];
}

// Sorted -> Binary Search
// time complexity: O(nlogn) || space complexity: O(1)
function twoSum2(numbers: number[], target: number): number[] {
  function binarySearch(array: number[], target: number): number {
    let start = 0;
    let end = array.length - 1;

    while (start <= end) {
      let midPointer = Math.floor((start + end) / 2);

      if (array[midPointer] > target) {
        end = midPointer - 1;
      } else if (array[midPointer] < target) {
        start = midPointer + 1;
      } else {
        return midPointer;
      }
    }

    return -1;
  }

  for (let i = 0; i < numbers.length; i++) {
    const complement = target - numbers[i];
    const result = binarySearch(numbers.slice(i + 1), complement);

    if (result >= 0) return [i + 1, i + 1 + result + 1];
  }

  return [-1, -1];
}

// Two Pointer
// time complexity: O(n) || space complexity: O(1)
function twoSum3(numbers: number[], target: number): number[] {
  let front = 0;
  let rear = numbers.length - 1;

  while (front < rear) {
    if (numbers[front] + numbers[rear] > target) {
      rear -= 1;
    } else if (numbers[front] + numbers[rear] < target) {
      front += 1;
    } else {
      return [front + 1, rear + 1];
    }
  }

  return [-1, -1];
}
