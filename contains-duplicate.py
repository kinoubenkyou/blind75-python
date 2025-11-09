class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_: set[int] = set()
        for number in nums:
            if number in set_:
                return True
            set_.add(number)
        return False
