class Solution:
    def canConstruct1(self, ransomNote: str, magazine: str) -> bool:
        magazine_list = list(magazine)

        for alphabet in ransomNote:
            if alphabet in magazine_list:
                magazine_list.remove(alphabet)
            else:
                return False

        return True

    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        magazine_alphabet_counter = {}
        for alphabet in magazine:
            if alphabet in magazine_alphabet_counter:
                magazine_alphabet_counter[alphabet] += 1
            else:
                magazine_alphabet_counter[alphabet] = 1

        for alphabet in ransomNote:
            if (
                alphabet in magazine_alphabet_counter
                and magazine_alphabet_counter[alphabet] > 0
            ):
                magazine_alphabet_counter[alphabet] -= 1
            else:
                return False

        return True
