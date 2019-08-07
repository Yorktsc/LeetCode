class Solution:
    def longestConsecutive(self, nums):
        hash_dict = dict()
        
        max_length = 0
        for num in nums:
            if num not in hash_dict:
                left = hash_dict.get(num - 1, 0)
                right = hash_dict.get(num + 1, 0)
                
                cur_length = 1 + left + right
                if cur_length > max_length:
                    max_length = cur_length
                
                hash_dict[num] = cur_length
                hash_dict[num - left] = cur_length
                hash_dict[num + right] = cur_length
                
        return max_length

	"""
	longest_streak = 0
        num_set = set(nums) #Changing a list into a hashset can speedup the time for access of elements

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
        """
        
        """
        if not nums:
            return 0

        nums.sort()

        longest_streak = 1
        current_streak = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1]+1:
                    current_streak += 1
                else:
                    longest_streak = max(longest_streak, current_streak)
                    current_streak = 1

        return max(longest_streak, current_streak)
        """
        
        """
        #([beg, end], len)
        #update when end meets beg
        res = []
        for num in nums:
            if not helper(res, num):
                res.append(([num-1, num+1], 1))
        res = sorted(res, key = lambda tup: tup[0][0])
        res2 = []
        i = 0 
        while i >= 0 and i < len(res) - 1:
            tup = res[i]
            tup2 = res[i+1]
            if tup[0][1] == tup2[0][0] + 1:
                res2.append(([tup[0][0], tup2[0][1]], tup[1] + tup2[1]))
                i += 2
            else:
                res2.append(tup)
                i += 1
        """
            
            
    def helper(res, num):
        for tup in res:
            if num in tup[0]:
                if num == tup[0][0]:
                    tup[0][0] = num - 1
                else:
                    tup[0][1] = num + 1
                num[1] += 1
                return True
        return False
        """
        size = len(nums)
        dp = [0] * size
        dp[0] = 1
        for i in range(1, size):
        """
