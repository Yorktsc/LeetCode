class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        flag = False
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] < nums[i]:
                k, j = i - 1, len(nums) - 1
                while nums[j] <= nums[k]:
                    j -= 1
                nums[k], nums[j] = nums[j], nums[k]
                start, end = i, len(nums) - 1
                while start < end:
                    nums[start], nums[end] = nums[end], nums[start]
                    start, end = start + 1, end - 1
                flag = True
                break
        if not flag:
            nums.reverse()
        """
        
        i = j = len(nums) - 1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0:
            nums.reverse()
            return
        k = i - 1
        while nums[j] <= nums[k]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]
        start, end = k+1, len(nums) - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1; end -= 1; 
        """
