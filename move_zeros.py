class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        """
        for i in nums[:]:
            if i==0:
                nums.append(0)
                nums.remove(0)
            
        """
        
        """
        nonzero = 0
        for num in nums:
            if num != 0:
                nums[nonzero] = num
                nonzero += 1
        while nonzero < len(nums):
            nums[nonzero] = 0
            nonzero += 1
        """
        
        i,j = 0,0
        while i < len(nums):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
            i += 1
