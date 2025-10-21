class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        stop = len(nums)
        while True:
            median_index = start + (stop - start) // 2
            median = nums[median_index]
            if median == target:
                return median_index
            elif median > target:
                if median_index == start:
                    return -1
                stop = median_index
            else:
                if median_index == stop - 1:
                    return -1
                start = median_index + 1
