#!/bin/python3

import math
import os
import random
import re
import sys

from typing import List


# Complete the countNumbers function below.
def countNumbers(arr):
    for numberRange in arr:
        count = getNotRepeatingCount(numberRange)

        print(count)


def getNotRepeatingCount(numberRange: List[int]) -> int:
    start, end = numberRange

    count = 0

    for number in range(start, end + 1):
        doesItInclude = doesItIncludeRepeating(number)

        if not doesItInclude:
            count += 1

    return count


def doesItIncludeRepeating(number: int) -> bool:
    numberStr = str(number)
    numberSet = set(numberStr)

    return len(numberStr) != len(numberSet)


if __name__ == "__main__":
    arr_rows = int(input().strip())
    arr_columns = int(input().strip())

    arr = []

    for _ in range(arr_rows):
        arr.append(list(map(int, input().rstrip().split())))

    countNumbers(arr)
