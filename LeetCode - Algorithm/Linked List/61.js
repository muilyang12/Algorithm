// 61. Rotate List
// https://leetcode.com/problems/rotate-list/

function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var rotateRight = function (head, k) {
  if (!head || k === 0) return head;

  let count = 0;
  let current = head;
  while (current) {
    current = current.next;
    count += 1;
  }

  const realK = k % count;

  if (realK === 0) return head;

  let fast = head;
  for (let i = 0; i < realK; i++) {
    fast = fast.next;
  }
  let slow = head;
  for (let i = 0; i < count - realK - 1; i++) {
    fast = fast.next;
    slow = slow.next;
  }

  let result = slow.next;
  slow.next = null;
  fast.next = head;

  return result;
};

/*
head = [1,2,3,4,5], k = 2
            ^   ^

head = [1], k = 1
        ^
        ^
*/
