const quickSort = (array: number[]): number[] => {
  if (array.length <= 1) return array;

  const pivot = array[array.length - 1];

  const leftArray: number[] = [];
  const rightArray: number[] = [];

  array.forEach((element) => {
    if (element < pivot) leftArray.push(element);
    else if (element > pivot) rightArray.push(element);
  });

  return [...quickSort(leftArray), pivot, ...quickSort(rightArray)];
};

const array = [5, 4, 3, 2, 1];
console.log(quickSort(array));
