from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                print("i--", i, "j--", j)
                if nums[j] == target - nums[i]:
                    return [i, j]
nums = [2, 7, 11, 15]
target = 9

solution = Solution()
result = solution.twoSum(nums, target)
print(result)