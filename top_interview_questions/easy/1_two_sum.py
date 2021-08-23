# 1. Two Sum problem: https://leetcode.com/problems/two-sum/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return [0, 1]


def check_hypothesis_for(hypothesis, nums, target):
    result = hypothesis.twoSum(nums, target)

    print(f'Input: nums = {nums}, target = {target}')
    print(f'Output: {result}')


if __name__ == '__main__':
    hypothesis = Solution()

    check_hypothesis_for(hypothesis, [2, 7, 11, 15], 9)
    check_hypothesis_for(hypothesis, [3, 2, 4], 6)
    check_hypothesis_for(hypothesis, [3, 3], 6)
