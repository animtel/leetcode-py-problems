
class Solution:
    def __init__(self):
        self.roman_to_int_pairs = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

    def romanToInt(self, s: str) -> int:
        result = 0
        prev_int_to_diff = 0

        for i in s:
            int_i = self.roman_to_int_pairs[i]

            if prev_int_to_diff < int_i:
                result += (int_i - prev_int_to_diff - prev_int_to_diff)
                prev_int_to_diff = int_i
            else:
                prev_int_to_diff = int_i
                result += int_i

        return result


def check_hypothesis_for(hypothesis, given, should):
    reversed = hypothesis.romanToInt(given)
    assert reversed == should, f'Wrong reverse for number {given}, returned: {reversed}, should be {should}!'


if __name__ == '__main__':
    hypothesis = Solution()

    check_hypothesis_for(hypothesis, 'III', 3)
    check_hypothesis_for(hypothesis, 'IV', 4)
    check_hypothesis_for(hypothesis, 'IX', 9)
    check_hypothesis_for(hypothesis, 'LVIII', 58)
    check_hypothesis_for(hypothesis, 'MCMXCIV', 1994)
