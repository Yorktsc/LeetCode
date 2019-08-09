class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = {1}
        while n not in seen:
            seen.add(n)
            n = sum(int(i) ** 2 for i in str(n))
        return n == 1

        """
        def helper(n):
            print(n)
            n_str = str(n)
            res = 0
            for index,num_str in enumerate(n_str):
                num = int(num_str)
                scale = len(n_str) - 1 - index
                res += num ** 2
            print(res)
            return res
        seen = set()
        if n == 1:
            return True
        if n not in seen:
            seen.add(n)
            n = helper(n)
            return self.isHappy(n)
        else:
            return False
        """
