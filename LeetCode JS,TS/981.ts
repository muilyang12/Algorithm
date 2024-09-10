// 981. Time Based Key-Value Store
// https://leetcode.com/problems/time-based-key-value-store/

interface Value {
  value: string;
  timestamp: number;
}

// Brute Force
// time complexity: O(n) for set and O(n) for get
class TimeMap1 {
  data: Map<string, Value[]>;

  constructor() {
    this.data = new Map<string, Value[]>();
  }

  set(key: string, value: string, timestamp: number): void {
    if (!this.data.has(key)) {
      this.data.set(key, [{ value, timestamp }]);

      return;
    }

    const existingValues: Value[] = this.data.get(key) as Value[];
    for (let i = 0; i < existingValues.length; i++) {
      if (timestamp > existingValues[i].timestamp) continue;

      const leftValues = existingValues.slice(0, i);
      const rightValues = existingValues.slice(i);
      const newValues = [...leftValues, { value, timestamp }, ...rightValues];

      this.data.set(key, newValues);
      return;
    }

    const newValues = existingValues.concat([{ value, timestamp }]); // time complexity: O(n)
    this.data.set(key, newValues);
  }

  get(key: string, timestamp: number): string {
    const values = this.data.get(key);

    if (!values) return "";

    for (let i = 0; i < values.length; i++) {
      if (timestamp >= values[i].timestamp) continue;

      if (i - 1 < 0) return "";

      return values[i - 1].value;
    }

    return values[values.length - 1].value;
  }
}

// Binary Search
// time complexity: O(logn) for set and O(logn) for get
class TimeMap2 {
  data: Map<string, Value[]>;

  constructor() {
    this.data = new Map<string, Value[]>();
  }

  set(key: string, value: string, timestamp: number): void {
    if (!this.data.has(key)) {
      this.data.set(key, [{ value, timestamp }]);

      return;
    }

    const existingValues: Value[] = this.data.get(key) as Value[];

    let left = 0;
    let right = existingValues.length - 1;

    while (left <= right) {
      const mid = Math.floor((left + right) / 2);

      if (mid + 1 >= existingValues.length) break;

      if (
        timestamp >= existingValues[mid].timestamp &&
        timestamp < existingValues[mid + 1].timestamp
      ) {
        const leftValues = existingValues.slice(0, mid + 1);
        const rightValues = existingValues.slice(mid + 1);
        const newValues = [...leftValues, { value, timestamp }, ...rightValues];
        this.data.set(key, newValues);

        return;
      } else if (timestamp < existingValues[mid].timestamp) {
        right = mid - 1;
      } else {
        left = mid + 1;
      }
    }

    existingValues.push({ value, timestamp });
    this.data.set(key, existingValues);
  }

  get(key: string, timestamp: number): string {
    const values = this.data.get(key);

    if (!values) return "";

    let left = 0;
    let right = values.length - 1;

    while (left <= right) {
      const mid = Math.floor((left + right) / 2);

      if (mid + 1 >= values.length) break;

      if (
        timestamp >= values[mid].timestamp &&
        timestamp < values[mid + 1].timestamp
      ) {
        return values[mid].value;
      } else if (timestamp < values[mid].timestamp) {
        right = mid - 1;
      } else {
        left = mid + 1;
      }
    }

    if (timestamp < values[values.length - 1].timestamp) return "";
    else return values[values.length - 1].value;
  }
}
