class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtyp: List[int]
        """
        return self.heapSort(nums)
        
        
        
    def mergeSort(self, nums):
        if len(nums) == 1:
            return nums
        size = len(nums)
        left, right = self.mergeSort(nums[:size//2]), self.mergeSort(nums[size//2:])
        res = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            l, r = left[i], right[j]
            if l < r:
                res.append(l)
                i += 1
            else:
                res.append(r)
                j += 1
        res = res + left[i:] if i < len(left) else res + right[j:]
        return res
        
    def quickSort(self, nums):
        size = len(nums)
        if size <= 1:
            return nums
        pivot = nums[-1]
        low, high = [], []
        for num in nums[:-1]:
            if num <= pivot:
                low.append(num)
            else:
                high.append(num)
        return self.quickSort(low) + [pivot] + self.quickSort(high)
    
    def heapSort(self, nums):
        def heapify(start,end):
            node = start
            while True:
                child = node * 2 + 1
                if child > end:
                    break
                if child + 1 <= end and nums[child] < nums[child + 1]:
                    child += 1
                if nums[node] < nums[child]:
                    nums[node], nums[child] = nums[child], nums[node]
                    node = child
                else:
                    break
        for i in xrange((len(nums)-1)//2, -1, -1):
            heapify(i, len(nums) - 1)
        for end in xrange(len(nums)-1, -1, -1):
            nums[0], nums[end] = nums[end], nums[0]
            heapify(0, end-1)
        return nums
