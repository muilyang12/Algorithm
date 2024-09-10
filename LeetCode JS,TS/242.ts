// 242. Valid Anagram
// https://leetcode.com/problems/valid-anagram/

// Sorting (Merge Sort)
// time complexity: O(nlogn) || space complexity: O(n)
function isAnagram1(s: string, t: string): boolean {
  if (s.length !== t.length) return false;

  const sArr = s.split("");
  mergeSort(sArr, 0, sArr.length - 1);
  const tArr = t.split("");
  mergeSort(tArr, 0, tArr.length - 1);

  for (let i = 0; i < sArr.length; i++) {
    if (sArr[i] !== tArr[i]) return false;
  }

  return true;

  // Merge Sort
  // time complexity O(nlogn)
  function mergeSort(str: string[], start: number, end: number) {
    if (start < end) {
      const mid = Math.floor((start + end) / 2);

      mergeSort(str, start, mid);
      mergeSort(str, mid + 1, end);

      merge(str, start, mid, end);
    }
  }

  function merge(str: string[], start: number, mid: number, end: number) {
    let i = start;
    let j = mid + 1;

    const result: string[] = [];

    while (i <= mid && j <= end) {
      if (str[i] < str[j]) {
        result.push(str[i]);
        i++;
      } else {
        result.push(str[j]);
        j++;
      }
    }

    while (i <= mid) {
      result.push(str[i]);
      i++;
    }

    while (j <= end) {
      result.push(str[j]);
      j++;
    }

    result.forEach((char, index) => {
      str[start + index] = char;
    });
  }
}

// Hash Table
// time complexity: O(2n) = O(n) || space complexity: O(n)
function isAnagram2(s: string, t: string): boolean {
  if (s.length !== t.length) return false;

  const hashTable = {};

  for (let i = 0; i < s.length; i++) {
    if (!hashTable[s[i]]) {
      hashTable[s[i]] = 1;

      continue;
    }

    hashTable[s[i]] += 1;
  }

  for (let i = 0; i < t.length; i++) {
    if (!hashTable[t[i]]) return false;

    hashTable[t[i]] -= 1;
  }

  return true;
}
