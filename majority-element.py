class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = 0, 0
        for number in nums:
            if count == 0:
                candidate = number
            if number == candidate:
                count += 1
            else:
                count -= 1
        return candidate
