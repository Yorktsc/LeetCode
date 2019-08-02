class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        L = matrix[0][0]
        R = matrix[n-1][n-1]
        res = 0
        while L <= R:
            mid = L + ((R - L) >> 1)
            if self.helper(matrix, mid, n, k):
                res = mid
                L = mid + 1
            else:
                R = mid - 1
        return res
        
    def helper(self, matrix, m, n, k):
        sum_ = 0
        for i in range(n):
            l, r, ans = 0, n-1, 0
            while l <= r:
                mid = l + ((r - l) >> 1)
                if matrix[i][mid] < m:
                    ans = mid + 1
                    l = mid + 1
                else:
                    r = mid - 1
            sum_ += ans
        return k > sum_
