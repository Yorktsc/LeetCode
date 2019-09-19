class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #dp approach
        """
        tmp = nums[0]
        res = tmp
        size = len(nums)
        for i in xrange(1,size):
            if nums[i] > tmp + nums[i]:
                tmp = nums[i]
            else:
                tmp += nums[i]
            res = max(res, tmp)
        return res
        """
        
        #divide and conquer
        size = len(nums)
        if size == 1:
            return nums[0]
        max_left = self.maxSubArray(nums[size//2:])
        max_right = self.maxSubArray(nums[:size//2])
        max_l = nums[size//2 - 1]
        max_r = nums[size//2]
        tmp = 0
        for i in range(size//2 - 1, -1, -1):
            tmp += nums[i]
            max_l = max(max_l, tmp)
        tmp = 0
        for i in range(size//2, size):
            tmp += nums [i]
            max_r = max(max_r, tmp)
        return max(max_left, max_right, max_l + max_r)
