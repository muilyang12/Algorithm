// 19. Remove Nth Node From End of List
// https://leetcode.com/problems/remove-nth-node-from-end-of-list/

function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
// time complexity: O(n)
// space complexity: O(1)
var removeNthFromEnd = function (head, n) {
  let nodeBeforeSlow = null;
  let slow = head;
  let fast = head;

  for (let i = 0; i < n; i++) {
    fast = fast.next;
  }

  while (fast) {
    fast = fast.next;
    nodeBeforeSlow = slow;
    slow = slow.next;
  }

  if (!nodeBeforeSlow) return slow.next;

  nodeBeforeSlow.next = slow.next;

  return head;
};
