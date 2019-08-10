class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        counter = 1
        res = ""
        length = [len(s) for s in strs]
        while counter <= min(length):
            prefix = strs[0][:counter]
            for ss in strs[1:]:
                if ss[:counter] == prefix:
                    continue
                else:
                    return res
            counter += 1 
            res = prefix
        return res
