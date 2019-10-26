class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        nums.sort()
        res = 0
        min_ = float("inf")
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: continue 
            j,k = i+1, len(nums)-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                diff = abs(target - s)
                if diff < min_:
                    min_ = diff
                    res = s
                    print(res)
                if s < target:
                    j += 1
                    while j < k and nums[j] == nums[j-1]: j += 1
                elif s > target:
                    k -= 1
                    while j < k and nums[k] == nums[k+1]: k -= 1
                else:
                    return target
        return res
