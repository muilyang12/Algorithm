// 21. Merge Two Sorted Lists
// https://leetcode.com/problems/merge-two-sorted-lists/

// Merge Sort
// time complexity: O(m + n) || space complexity: O(1)
function mergeTwoLists1(
  list1: ListNode | null,
  list2: ListNode | null
): ListNode | null {
  if (!list1 && !list2) return null;

  const dummy: ListNode = new ListNode();
  let resultPointer: ListNode = dummy;

  let list1Pointer = list1;
  let list2Pointer = list2;

  while (list1Pointer && list2Pointer) {
    if (list1Pointer.val <= list2Pointer.val) {
      resultPointer.next = list1Pointer;
      list1Pointer = list1Pointer.next;
    } else {
      resultPointer.next = list2Pointer;
      list2Pointer = list2Pointer.next;
    }

    resultPointer = resultPointer.next;
  }

  while (list1Pointer) {
    resultPointer.next = list1Pointer;
    resultPointer = resultPointer.next;

    list1Pointer = list1Pointer.next;
  }

  while (list2Pointer) {
    resultPointer.next = list2Pointer;
    resultPointer = resultPointer.next;

    list2Pointer = list2Pointer.next;
  }

  return dummy.next;
}

// Merge Sort
// time complexity: O(m + n) || space complexity: O(n + m)
function mergeTwoLists2(
  list1: ListNode | null,
  list2: ListNode | null
): ListNode | null {
  if (!list1 && !list2) return null;

  const dummy: ListNode = new ListNode();
  let resultPointer: ListNode = dummy;

  let list1Pointer = list1;
  let list2Pointer = list2;

  while (list1Pointer && list2Pointer) {
    if (list1Pointer.val <= list2Pointer.val) {
      resultPointer.next = new ListNode(list1Pointer.val);
      resultPointer = resultPointer.next;

      list1Pointer = list1Pointer.next;
    } else {
      resultPointer.next = new ListNode(list2Pointer.val);
      resultPointer = resultPointer.next;

      list2Pointer = list2Pointer.next;
    }
  }

  while (list1Pointer) {
    resultPointer.next = new ListNode(list1Pointer.val);
    resultPointer = resultPointer.next;

    list1Pointer = list1Pointer.next;
  }

  while (list2Pointer) {
    resultPointer.next = new ListNode(list2Pointer.val);
    resultPointer = resultPointer.next;

    list2Pointer = list2Pointer.next;
  }

  return dummy.next;
}

class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}
