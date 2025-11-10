class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ = max_ending_at_last_number = nums[0]
        for number in nums[1:]:
            if number > max_ending_at_last_number + number:
                max_ending_at_last_number = number
            else:
                max_ending_at_last_number += number
            if max_ending_at_last_number > max_:
                max_ = max_ending_at_last_number
        return max_
