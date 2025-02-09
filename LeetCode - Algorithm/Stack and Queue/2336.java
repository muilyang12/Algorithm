// 2336. Smallest Number in Infinite Set
// https://leetcode.com/problems/smallest-number-in-infinite-set/

import java.util.PriorityQueue;
import java.util.Set;
import java.util.HashSet;

class SmallestInfiniteSet {
    PriorityQueue<Integer> minHeap;
    int numberWhenEmpty;
    Set<Integer> set;

    public SmallestInfiniteSet() {
        this.minHeap = new PriorityQueue<>();
        this.numberWhenEmpty = 1;
        this.set = new HashSet<>();
    }

    public int popSmallest() {
        int result;

        if (this.minHeap.isEmpty()) {
            result = numberWhenEmpty;
            numberWhenEmpty++;
        } else {
            result = this.minHeap.poll();
            this.set.remove(result);
        }

        return result;
    }

    public void addBack(int num) {
        if (num >= this.numberWhenEmpty)
            return;

        if (this.set.contains(num))
            return;

        this.set.add(num);
        this.minHeap.offer(num);
    }
}