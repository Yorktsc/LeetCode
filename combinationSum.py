class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        candidates = sorted(candidates)
        def dfs(nums, curr_set, curr_sum):
            for i in range(len(nums)):
                temp_sum = nums[i] + curr_sum
                if temp_sum == target:
                    ans.append(curr_set + [nums[i]])
                elif temp_sum > target:
                    return
                else:
                    dfs(nums[i:], curr_set + [nums[i]], temp_sum)
        
        dfs(candidates, [], 0)
        
        return ans
