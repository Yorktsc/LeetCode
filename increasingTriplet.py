class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # [5,2,6,3,5,4]
        one = float("inf")
        two = float("inf")
        for num in nums:
            if num <= one:
                one = num
            elif num <= two:
                two = num
            else:
                return True
        return False
        
        # Longest Increasing Sequence
        """
        size = len(nums)
        dp = [1] * size
        for index, num in enumerate(nums):
            if index == 0:
                continue
            res = []
            for ii, nn in enumerate(nums[:index]):
                if nn < num:
                    res.append(dp[ii])
            dp[index] = max(res) + 1 if res else 1
            if dp[index] >= 3:
                return True
        """
