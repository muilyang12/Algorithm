// 139. Word Break
// https://leetcode.com/problems/word-break/

// Divide-and-conquer
// time complexity: O(n^3) || space complexity: O(n)
function wordBreak(s: string, wordDict: string[]): boolean {
  let result = false;

  const cuttingPoint: number[] = [];
  let end = 0;
  while (end < s.length) {
    const target = s.slice(0, end + 1);
    if (wordDict.includes(target)) cuttingPoint.push(end);

    end++;
  }

  if (cuttingPoint.length === 0) return false;

  for (let i = 0; i < cuttingPoint.length; i++) {
    const nextString = s.slice(cuttingPoint[i] + 1);
    if (nextString === "") return true;

    result = result || wordBreak1(nextString, wordDict);
  }

  return result;
}
