# 14. Longest Common Prefix: https://leetcode.com/problems/longest-common-prefix/

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        def subtract_to_pref(str_a, str_b):
            common_pref = ''

            len_a, len_b = len(str_a), len(str_b)
            if len_a > len_b:
                len_a, len_b = len_b, len_a

            if len_a == 0 or len_b == 0:
                return ''

            for i in range(len_a):
                if str_a[i] == str_b[i]:
                    common_pref += str_a[i]
                else:
                    break

            return common_pref

        def rec_loop(strs: List[str], pref):
            if len(strs) == 1:
                return subtract_to_pref(strs[0], pref)

            return rec_loop(strs[1:], subtract_to_pref(strs[0], pref))

        return rec_loop(strs[1:], strs[0])


def check_hypothesis_for(hypothesis_func, given, should):
    reversed = hypothesis_func(given)
    assert reversed == should, f'Wrong hypothesis for {given}, returned: {reversed}, should be {should}!'

if __name__ == '__main__':
    hypothesis = Solution().longestCommonPrefix

    check_hypothesis_for(hypothesis, ["flower","flow","flight"], 'fl')
    check_hypothesis_for(hypothesis, ["dog","racecar","car"], '')
    check_hypothesis_for(hypothesis, ["aaa","aa","aaa"], 'aa')
    check_hypothesis_for(hypothesis, [""], '')