# 14. Longest Common Prefix: https://leetcode.com/problems/longest-common-prefix/

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ''
        min_str = min(strs)
        max_str = max(strs)

        for i in range(len(min_str)):
            if min_str[i] != max_str[i]:
                return min_str[:i]

        return min_str



def check_hypothesis_for(hypothesis_func, given, should):
    reversed = hypothesis_func(given)
    assert reversed == should, f'Wrong hypothesis for {given}, returned: {reversed}, should be {should}!'

if __name__ == '__main__':
    hypothesis = Solution().longestCommonPrefix

    check_hypothesis_for(hypothesis, ["flower","flow","flight"], 'fl')
    check_hypothesis_for(hypothesis, ["dog","racecar","car"], '')
    check_hypothesis_for(hypothesis, ["aaa","aa","aaa"], 'aa')
    check_hypothesis_for(hypothesis, [""], '')
