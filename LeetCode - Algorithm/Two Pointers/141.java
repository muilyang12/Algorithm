// 141. Linked List Cycle
// https://leetcode.com/problems/linked-list-cycle/

class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
        next = null;
    }
}

// time complexity: O(n)
// space complexity: O(1)
class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null)
            return false;

        ListNode slow = head;
        ListNode fast = head;

        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;

            if (slow == fast)
                return true;
        }

        return false;
    }
}

/*
 * The algorithm I used here is called Floyd's cycle detection algorithm. When I
 * solved this problem last time, I used a HashMap because I thought the
 * two-pointer approach might not be suitable. However, recently, I encountered
 * problem 287, where I had to use Floyd's cycle detection algorithm. That
 * problem involved finding the starting node of a cycle in a graph. So, I
 * wanted to revisit this question and solve it again using Floyd's cycle
 * detection approach.
 */