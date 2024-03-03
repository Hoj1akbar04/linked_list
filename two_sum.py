
"""class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, num in enumerate(nums):
            a = target - num
            if a in dict:
                return [dict[a], i]
            dict[num] = i
        return [-1, -1]"""


def two_sum(nums, target):
    dict = {}
    for i, num in enumerate(nums):
        a = target - num
        if a in dict:
            return [dict[a], i]
        dict[num] = i
    return []


# Example usage:
nums = [2, 7, 11, 15]
target = 13
print(two_sum(nums, target))
