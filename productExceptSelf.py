class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #top triangle corresponds to the product of items on the left
        res, p, q = [1], 1, 1
        for i in range(len(nums) - 1): # top triangle
            p *= nums[i]
            res.append(p)
            print(res)
        #bottom triangle corresponds to the product of items on the right
        for i in range(len(nums) - 1, 0, -1): # bottom triangle
            q *= nums[i]
            res[i - 1] *= q
            print(res)
        return res
