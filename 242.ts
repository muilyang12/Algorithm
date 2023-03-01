// 242. Valid Anagram
// https://leetcode.com/problems/valid-anagram/

// Sorting (Merge Sort)
// time complexity: O(O(nlogn) || space complexity: O(2n) = O(n)
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
