class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if '[' not in s:
            return s
        res, start, end = '', 0, len(s)
        while start < end:
            c = s[start]
            if c.isdigit():
                tmp_int = start + 1
                while tmp_int < end:
                    if s[tmp_int].isdigit():
                        tmp_int += 1
                    else:
                        break
                multi = int(s[start:tmp_int])
                start = tmp_int + 1
                left = 1
                right = 0
                for i in range(start, end):
                    char = s[i]
                    if char == '[':
                        left += 1
                    if char == ']':
                        right += 1
                    if left == right:
                        tmp = self.decodeString(s[start:i])
                        res += multi * tmp
                        start = i + 1
                        break
            else:
                res += s[start]
                start += 1
                continue
        return res
