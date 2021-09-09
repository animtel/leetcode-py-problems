# 26. Remove Duplicates from Sorted Array: https://leetcode.com/problems/remove-duplicates-from-sorted-array/


from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_len = len(nums)

        if len(nums) == 0: return 0

        k = 1

        for i in range(1, nums_len):
            if nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k += 1

        return k


def check_hypothesis_for(hypothesis_func, given, should):
    processed = hypothesis_func(given)
    k, expected_nums = should

    assert processed == k, f'Wrong length, returned: {processed}, should be: {k}'

    for i in range(k):
        assert given[i] == expected_nums[i], f'Wrong array, returned: {given}, should be: {expected_nums}'


if __name__ == '__main__':
    hypothesis = Solution().removeDuplicates
    check_hypothesis_for(hypothesis, [1, 1, 2], (2, [1, 2]))  # should be len 2 and changed by pointer nums: [1, 2]

    check_hypothesis_for(hypothesis, [0, 0, 1, 1, 1, 2, 2, 3, 3, 4], (5, [0, 1, 2, 3, 4]))
