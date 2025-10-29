class Solution:
    def climbStairs(self, n: int) -> int:
        last, second_last = 1, 0
        for _ in range(1, n):
            last, second_last = last + second_last, last
        return last + second_last
