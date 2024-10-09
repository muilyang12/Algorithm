// 380. Insert Delete GetRandom O(1)
// https://leetcode.com/problems/insert-delete-getrandom-o1/

class RandomizedSet {
  valueToIndex: Record<string, number>;
  values: number[];

  constructor() {
    this.valueToIndex = {};
    this.values = [];
  }

  insert(val: number): boolean {
    if (this.valueToIndex[val] !== undefined) return false;

    this.values.push(val);
    this.valueToIndex[val] = this.values.length - 1;

    return true;
  }

  remove(val: number): boolean {
    if (this.valueToIndex[val] === undefined) return false;

    const targetIndex = this.valueToIndex[val];
    const lastValue = this.values.pop() ?? -1;
    delete this.valueToIndex[val];

    if (val === lastValue) return true;

    this.values[targetIndex] = lastValue;
    this.valueToIndex[lastValue] = targetIndex;

    return true;
  }

  getRandom(): number {
    const randomIndex = Math.floor(Math.random() * this.values.length);

    return this.values[randomIndex];
  }
}
