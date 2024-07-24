# 399. Evaluate Division
# https://leetcode.com/problems/evaluate-division/


from typing import List


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        value_data = {}

        for index, equation in enumerate(equations):
            first, second = equation

            if not first in value_data and not second in value_data:
                value_data[first] = (values[index], second)
                value_data[second] = (1, second)

            elif first in value_data and not second in value_data:
                coefficient, alphabet = value_data[first]
                value_data[second] = ((1 / values[index]) * coefficient, alphabet)

            elif not first in value_data and second in value_data:
                coefficient, alphabet = value_data[second]
                value_data[first] = (values[index] * coefficient, alphabet)

            else:
                first_coeff, first_alpha = value_data[first]
                second_coeff, second_alpha = value_data[second]

                # fa = values[index] * sc * 1 / fc * sa

                if first_alpha == second_alpha:
                    continue

                for key, value in value_data.items():
                    value_coeff, value_alpha = value

                    if value_alpha != first_alpha:
                        continue

                    value_data[key] = (
                        value_coeff * values[index] * second_coeff * (1 / first_coeff),
                        second_alpha,
                    )

                print(value_data[first], value_data[second])

        result = []

        for query in queries:
            first, second = query

            if not first in value_data or not second in value_data:
                result.append(-1)
            else:
                first_coeff, first_alpha = value_data[first]
                second_coeff, second_alpha = value_data[second]

                if first_alpha == second_alpha:
                    result.append(first_coeff / second_coeff)
                else:
                    result.append(-1)

        return result
