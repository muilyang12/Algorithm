// 160. Intersection of Two Linked Lists
// https://leetcode.com/problems/intersection-of-two-linked-lists/

import java.util.Set;
import java.util.HashSet;

class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
        next = null;
    }
}

class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode currentA = headA;
        ListNode currentB = headB;

        Set<ListNode> nodesInA = new HashSet<>();

        while (currentA != null) {
            nodesInA.add(currentA);

            currentA = currentA.next;
        }

        while (currentB != null) {
            if (nodesInA.contains(currentB))
                return currentB;

            currentB = currentB.next;
        }

        return null;
    }
}