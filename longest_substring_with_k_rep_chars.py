class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        """
        def split(sub, k):
            from collections import Counter
            if len(sub) < k:
                return 0
            res = Counter(sub)
            print(res)
            for key, val in res.items():
                #print(key)
                #print(val)
                if val < k:
                    index = sub.index(key)
                    left, right = sub[:index], sub[index+1:]
                    #print("left: {}".format(left))
                    #print("right: {}".format(right))
                    l, r = split(left, k), split(right, k)
                    return max(l,r)
            return len(sub)
        return split(s, k)
        """
        if len(s)<k:
            return 0
        for i in set(s):
            if s.count(i)<k:
                return max(self.longestSubstring(sub,k) for sub in s.split(i))
        return len(s)
