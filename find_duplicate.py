class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l, h = 0, len(nums) - 1
        while l < h:
            m = (l + h) >> 1
            if sum(n <= m for n in nums) > m:
                h = m
            else:
                l = m + 1
        return l
