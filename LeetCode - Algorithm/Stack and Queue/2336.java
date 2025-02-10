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

/*
 * In order to use Min Heap, we can use PriorityQueue in Java.
 * 
 * PriorityQueue<Integer> minHeap = new PriorityQueue<>();
 * 
 * 1. To add an element -> offer() / add()
 * -> add() throws an exception if the queue is full
 * 2. To retrieve and remove the minimum element -> poll() / remove()
 * -> remove() throws an exception if the queue is empty.
 * 3. To retrieve the minimum element without removing it -> peek() / element()
 * -> element() throws an exception if the queue is empty.
 */

/*
 * In Java,
 * 
 * - "int" is a primitive type, which is a basic data type in Java designed for
 * efficiency.
 * - "Integer" is a Wrapper Class, which is an object that wraps the primitive
 * int and provides additional functionality.
 * 
 * Generics (like Stack<T>) do not support primitive types such as int and can
 * only work with objects. So, we should use the wrapper class "Integer" not
 * "int".
 */