// 82. Remove Duplicates from Sorted List II
// https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteDuplicates = function (head) {
  if (!head) return head;

  const dummy = new ListNode(-1);
  let current = dummy;

  let slow = head;
  let fast = head;

  while (fast.next) {
    if (fast.val === fast.next.val) {
      fast = fast.next;
    } else if (slow === fast) {
      current.next = fast;
      current = current.next;
      current.next = null;

      slow = fast.next;
      fast = fast.next;

      current.next = null;
    } else {
      slow = fast.next;
      fast = fast.next;
    }
  }

  if (slow === fast) {
    current.next = fast;
    current = current.next;
  }

  return dummy.next;
};

/*
head = [1,2,3,3,4,4,5]
                    ^

head = [1,1,1,2,3]
                ^

head = [1,2,2]
          ^ ^
*/
