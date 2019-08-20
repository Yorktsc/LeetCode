class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0: return []
        m = {'2':'abc', '3':'def','4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        size = len(digits)
        res = []
        def backtrack(digits, index, curr, res):
            if index == size:
                res.append(curr)
                return
            digit = digits[index]
            candidates = m[digit]
            for char in candidates:
                tmp = curr
                tmp += char
                backtrack(digits, index+1, tmp, res)
        backtrack(digits, 0, "", res)
        return res
