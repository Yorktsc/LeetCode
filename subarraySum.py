from collections import defaultdict
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        """
        #Approach1, Comulative Sum
        count,size = 0, len(nums)
        sum_list = [0]
        for i in range(1,size + 1):
            sum_list.append(sum_list[i-1] + nums[i - 1])
        for i in range(size):
            for j in range(i + 1,size + 1):
                if sum_list[j] - sum_list[i] == k:
                    count += 1
        print(sum_list)
        return count
        """
        
        """
        #Approach2, Optimized Brute Force
        count,size = 0, len(nums)
        for i in range(size):
            s = 0
            for j in range(i, size):
                s += nums[j]
                if s == k:
                    count += 1
        return count
        """
        
        #Approach3, Hashmap
        """
        count,size, s = 0, len(nums), 0
        m = {}
        m[0] = 1
        for i in range(size):
            s += nums[i]
            if s - k in m.keys():
                count += m[s-k]
            if s in m.keys():
                m[s] += 1
            else:
                m[s] = 1
        return count
        """
        pre_sum=0
        record=defaultdict(int)
        record[0]=1
        res=0
        for i in range(len(nums)):
            pre_sum+=nums[i]
            res+=record[pre_sum-k]
            record[pre_sum]+=1
        return res

