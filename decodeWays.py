class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        res = []
        def isValid(num):
            return 1 <= int(num) <= 26
        def backtrack(s):
            print(s)
            print(isValid(s))
            if isValid(s):
                res.append(0)
            if isValid(s[0]):
                backtrack(s[1:])
            if isValid(s[:2]):
                backtrack(s[2:])
        backtrack(s)
        return len(res)
        """
        
        """
        pp, p = 1, int(s[0] != '0')
        for i in range(1, len(s)):
            pp, p = p, pp * (9 < int(s[i-1:i+1]) <= 26) + p * (int(s[i]) > 0)
        return p
        """
        
        #DP
        if not s: return 0
        dp = [1] + [0] * (len(s)-1)
        if s[0] == "0": return 0
        if len(s)==1: return dp[0]
        if s[1] != "0":
            dp[1] += 1
        if 10 <= int(s[:2]) <= 26:
            dp[1] += 1
        for i in range(2, len(s)):
            if s[i-1] + s[i] == "00": return 0
            if s[i] != "0": dp[i] += dp[i-1]
            if 10 <= int(s[i-1] + s[i]) <= 26: dp[i] += dp[i-2]
        return dp[-1]
        
        
        
        #DP2
        """
        if not s:
            return 1
        ans = 0
        if len(s) >= 1 and s[0] != '0':
            ans += self.numDecodings(s[1:])
        if len(s) >= 2 and s[0] != '0' and int(s[:2]) <= 26:
            ans += self.numDecodings(s[2:])
        return ans
        """
