import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        ## N + K * Log N
        """
        nums = [-num for num in nums]
        heapq.heapify(nums)
        res = float('inf')
        for _ in range(k):
            res = heapq.heappop(nums)
        return -res
        """
        
        ## MinHeap N * Log K
        h = nums[:k]
        heapq.heapify(h)
        for num in nums[k:]:
            if num > h[0]:
                heapq.heappop(h)
                heapq.heappush(h, num)
        return h[0]
