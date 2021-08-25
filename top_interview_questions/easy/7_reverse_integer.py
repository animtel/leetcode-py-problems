# 1. Two Sum problem: https://leetcode.com/problems/reverse-integer/
from typing import List


class Solution:
    def reverse(self, x: int) -> int:
        max_size = (2**31)-1
        min_size = -2**31

        use_neg_sign = False

        if x < 0:
            use_neg_sign = True
            x *= -1

        rev = 0
        while x >= 1:
            pop = x % 10
            x /= 10

            if rev >= max_size or rev <= min_size: return 0

            rev = int(rev * 10 + pop)

        if use_neg_sign:
            rev *= -1

        if rev >= max_size or rev <= min_size:
            return 0

        return rev


def check_hypothesis_for(hypothesis, given, should):
    reversed = hypothesis.reverse(given)
    assert reversed == should, f'Wrong reverse for number {given}, returned: {reversed}, should be {should}!'



if __name__ == '__main__':
    hypothesis = Solution()

    # check_hypothesis_for(hypothesis, 1534236469, 0)
    # check_hypothesis_for(hypothesis, 123, 321)
    check_hypothesis_for(hypothesis, -123, -321)
    check_hypothesis_for(hypothesis, 120, 21)
    check_hypothesis_for(hypothesis, 0, 0)
