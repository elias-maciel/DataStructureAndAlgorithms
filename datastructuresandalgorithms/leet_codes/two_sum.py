from typing import List


class Solution:
    def bad_solution(self, nums: List[int], target: int) -> List[int]:
        for idx1, num1 in enumerate(nums):
            for idx2, num2 in enumerate(nums[idx1:]):
                if num1 + num2 == target:
                    return [idx1, idx2]

    def two_sum(self, nums: List[int], target: int) -> List[int]:
        hasher = {}
        for idx, i in enumerate(nums):
            if hasher.get(i) is not None:
                return [hasher.get(i), idx]
            hasher[target - i] = idx


if __name__ == '__main__':
    solution = Solution()
    print(solution.bad_solution([1, 2, 3], 4))
