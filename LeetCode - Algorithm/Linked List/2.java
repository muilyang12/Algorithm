// 2. Add Two Numbers
// https://leetcode.com/problems/add-two-numbers/

class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode currentL1 = l1;
        ListNode currentL2 = l2;

        ListNode dummy = new ListNode(-1);
        ListNode current = dummy;

        int carry = 0;

        while (currentL1 != null || currentL2 != null) {
            int value = 0;
            value += (currentL1 != null) ? currentL1.val : 0;
            value += (currentL2 != null) ? currentL2.val : 0;
            value += carry;

            boolean hasCarry = false;

            if (value >= 10) {
                hasCarry = true;
                value = value % 10;
            } else {
                hasCarry = false;
            }

            if (currentL1 != null)
                currentL1 = currentL1.next;

            if (currentL2 != null)
                currentL2 = currentL2.next;

            current.next = new ListNode(value);
            current = current.next;

            if (hasCarry)
                carry = 1;
            else
                carry = 0;
        }

        if (carry > 0) {
            current.next = new ListNode(carry);
        }

        return dummy.next;
    }
}