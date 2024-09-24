// 21. Merge Two Sorted Lists
// https://leetcode.com/problems/merge-two-sorted-lists/

function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function (list1, list2) {
  let first = list1;
  let second = list2;

  const dummy = new ListNode(-1);
  let current = dummy;

  while (first || second) {
    if (!first) {
      current.next = second;
      second = second.next;
    } else if (!second) {
      current.next = first;
      first = first.next;
    } else {
      if (first.val > second.val) {
        current.next = second;
        second = second.next;
      } else {
        current.next = first;
        first = first.next;
      }
    }

    current = current.next;
  }

  return dummy.next;
};
