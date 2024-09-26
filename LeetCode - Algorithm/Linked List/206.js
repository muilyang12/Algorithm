// 206. Reverse Linked List
// https://leetcode.com/problems/reverse-linked-list/

function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function (head) {
  let first = null;
  let second = head;
  let third = head?.next;

  while (second) {
    second.next = first;

    first = second;
    second = third;
    third = third?.next;
  }

  return first;
};
