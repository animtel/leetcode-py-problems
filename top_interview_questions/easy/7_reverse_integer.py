# 1. Two Sum problem: https://leetcode.com/problems/reverse-integer/
from typing import List


class Solution:
    def reverse(self, x: int) -> int:
        if (-2**31) >= x or x >= (2**31)-1:
            return 0

        str_x = str(x)
        sign = ''
        if str_x[0] == '-' and str_x[-1] == '0':
            sign = str_x[0]
            str_x = str_x[1:-1]
        elif str_x[0] == '-':
            sign = str_x[0]
            str_x = str_x[1:]

        str_x = str_x[::-1]

        x = int(sign + str_x)

        if (-2**31) >= x or x >= (2**31)-1:
            return 0

        return x


def check_hypothesis_for(hypothesis, given, should):
    reversed = hypothesis.reverse(given)
    assert reversed == should, f'Wrong reverse for number {given}, returned: {reversed}, should be {should}!'



if __name__ == '__main__':
    hypothesis = Solution()

    check_hypothesis_for(hypothesis, 1534236469, 0)
    check_hypothesis_for(hypothesis, 123, 321)
    check_hypothesis_for(hypothesis, -123, -321)
    check_hypothesis_for(hypothesis, 120, 21)
    check_hypothesis_for(hypothesis, 0, 0)
