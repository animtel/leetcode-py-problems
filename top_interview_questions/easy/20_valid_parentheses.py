#20. Valid Parentheses: https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        return False


def check_hypothesis_for(hypothesis_func, given, should):
    processed = hypothesis_func(given)
    assert reversed == should, f'Wrong hypothesis for given:{given}, returned: {processed}, should be {should}!'


if __name__ == '__main__':
    hypothesis = Solution().isValid

    check_hypothesis_for(hypothesis, '()', True)
    check_hypothesis_for(hypothesis, '()[]{}', True)
    check_hypothesis_for(hypothesis, '(]', False)
    check_hypothesis_for(hypothesis, '([)]', False)
    check_hypothesis_for(hypothesis, '{[]}', True)

