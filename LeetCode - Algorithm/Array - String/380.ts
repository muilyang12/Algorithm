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

`
If I use a Set, I can easily use 'has' and 'add' for inserting or removing elements. However, since Set does not 
support random access due to the lack of indexing, I can't use it here. So, to get a random value, I need to
maintain a 'values' array along with a 'valueToIndex' hash.
`;
