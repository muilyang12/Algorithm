const mergeSort = (arr: number[]): number[] => {
  if (arr.length === 1) return arr;

  const mid = Math.floor(arr.length / 2);

  const leftList = arr.slice(0, mid);
  const rightList = arr.slice(mid, arr.length - 1);

  mergeSort(leftList);
  mergeSort(rightList);

  const result: number[] = [];
  let leftIndex = 0;
  let rightIndex = 0;
  let mergedIndex = 0;

  while (leftIndex < leftList.length && rightIndex < rightList.length) {
    if (leftList[leftIndex] <= rightList[rightIndex]) {
      result.push(leftList[leftIndex]);

      leftIndex += 1;
      mergedIndex += 1;
    } else {
      result.push(rightList[rightIndex]);

      rightIndex += 1;
      mergedIndex += 1;
    }
  }

  // I wouldn't go into all the detailed logic for mergeSort.

  return result;
};
