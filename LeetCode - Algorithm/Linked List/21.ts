// 21. Merge Two Sorted Lists
// https://leetcode.com/problems/merge-two-sorted-lists/

class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
  const dummy = new ListNode(-1);
  let current = dummy;

  let first = list1;
  let second = list2;

  while (first || second) {
    if (!first && second) {
      current.next = second;
      current = current.next;
      second = second.next;
    } else if (first && !second) {
      current.next = first;
      current = current.next;
      first = first.next;
    } else if (first!.val >= second!.val) {
      current.next = second!;
      current = current.next;
      second = second!.next;
    } else {
      current.next = first!;
      current = current.next;
      first = first!.next;
    }
  }

  return dummy.next;
}
