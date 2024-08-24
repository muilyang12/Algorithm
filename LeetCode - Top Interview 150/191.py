# 67. Add Binary
# https://leetcode.com/problems/add-binary/


class Solution:
    def addBinary1(self, a: str, b: str) -> str:
        result = []

        reversed_a = a[::-1]
        reversed_b = b[::-1]

        length1 = len(a)
        length2 = len(b)

        carry = 0

        for i in range(min(length1, length2)):
            num1 = int(reversed_a[i])
            num2 = int(reversed_b[i])

            result.append(str((num1 + num2 + carry) % 2))

            carry = (num1 + num2 + carry) // 2

        if length1 > length2:
            for i in range(length2, length1):
                num1 = int(reversed_a[i])

                result.append(str((num1 + carry) % 2))

                carry = (num1 + carry) // 2

        elif length1 < length2:
            for i in range(length1, length2):
                num2 = int(reversed_b[i])

                result.append(str((num2 + carry) % 2))

                carry = (num2 + carry) // 2

        if carry > 0:
            result.append(str(carry))

        return "".join(list(reversed(result)))

    def addBinary2(self, a: str, b: str) -> str:
        result = ""

        i = len(a) - 1
        j = len(b) - 1

        carry = 0

        while i >= 0 or j >= 0 or carry != 0:
            current_sum = 0

            if i >= 0:
                current_sum += int(a[i])
                i -= 1

            if j >= 0:
                current_sum += int(b[j])
                j -= 1

            current_sum += carry

            carry = current_sum // 2
            result = str(current_sum % 2) + result

        return result
