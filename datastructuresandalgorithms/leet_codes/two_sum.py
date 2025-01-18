from typing import List


class Solution:
    def bad_solution(self, nums: List[int], target: int) -> List[int]:
        for idx, num1 in enumerate(nums):
            for num2 in nums[idx:]:
                if num1 + num2 == target:
                    return [num1, num2]


if __name__ == '__main__':
    solution = Solution()
    print(solution.bad_solution([1, 2, 3], 4))
