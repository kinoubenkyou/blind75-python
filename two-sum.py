class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_by_value: dict[int, int] = {}
        for index, value in enumerate(nums):
            complement_value = target - value
            if complement_value in index_by_value:
                return [index, index_by_value[complement_value]]
            if value not in index_by_value:
                index_by_value[value] = index
