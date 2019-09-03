class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :itype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            for i in range(len(res)):
                res.append(res[i][:] + [num])
        return res
