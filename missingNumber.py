class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        last = False
        first = False
        for num in nums:
            num = abs(num)
            if num == len(nums):
                last = True
            elif num == 0:
                first = True
            else:
                nums[num] = -nums[num]
        if not last:
            return len(nums)
        if not first:
            return 0
        for index in range(1,len(nums)):
            if nums[index] == 0:
                res = index
                continue
            if nums[index] > 0:
                return index
        return res
        """
        a = len(nums)*(len(nums)+1)/2
        b = sum(nums)
        return a - b
