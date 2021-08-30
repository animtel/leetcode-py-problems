#20. Valid Parentheses: https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        dict = {
            "[": "]",
            "{": "}",
            "(": ")"
        }
        opens = ['[', '{', '(']
        closed = [']', '}', ')']
        stack = []
        lst = list(s)
        if len(s) < 2:
            return False
        if lst[0] in closed or lst[-1] in opens:
            return False

        for i in range(len(lst)):
            if lst[i] in opens:
                stack.append(lst[i])
            else:
                if len(stack) != 0:
                    k = stack.pop()
                    if dict[k] != lst[i]:
                        return False
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False


def check_hypothesis_for(hypothesis_func, given, should):
    processed = hypothesis_func(given)
    assert processed == should, f'Wrong hypothesis for given:{given}, returned: {processed}, should be {should}!'


if __name__ == '__main__':
    hypothesis = Solution().isValid
    check_hypothesis_for(hypothesis, '()', True)
    check_hypothesis_for(hypothesis, '()[]{}', True)
    check_hypothesis_for(hypothesis, '(]', False)
    check_hypothesis_for(hypothesis, '([)]', False)
    check_hypothesis_for(hypothesis, '{[]}', True)

