# 1. Two Sum problem: https://leetcode.com/problems/two-sum/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        # Dictionary to store the difference and its index
        index_map = {}
        # Loop for each element
        for i, n in enumerate(nums):
            # Difference which needs to be checked
            difference = target - n
            if difference in index_map:
                result.append(i)
                result.append(index_map[difference])
                break
            else:
                index_map[n] = i

        return result


def check_hypothesis_for(hypothesis, nums, target):
    result = hypothesis.twoSum(nums, target)

    print(f'Input: nums = {nums}, target = {target}')
    print(f'Output: {result}')


if __name__ == '__main__':
    hypothesis = Solution()

    check_hypothesis_for(hypothesis, [2, 7, 11, 15], 9)
    check_hypothesis_for(hypothesis, [3, 2, 4], 6)
    check_hypothesis_for(hypothesis, [3, 3], 6)
