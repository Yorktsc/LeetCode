class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        """
        def valid(segment):
            return int(segment) <= 255 if segment[0] != '0' else len(segment) == 1
            
        def update_output(curr_pos):
            segment = s[curr_pos + 1:n]
            if valid(segment):
                segments.append(segment)
                output.append('.'.join(segments))
                segments.pop()    
            
        def backtrack(prev_pos = -1, dots = 3):
            # The current dot curr_pos could be placed 
            # in a range from prev_pos + 1 to prev_pos + 4.
            # The dot couldn't be placed 
            # after the last character in the string.
            for curr_pos in range(prev_pos + 1, min(n - 1, prev_pos + 4)):
                segment = s[prev_pos + 1:curr_pos + 1]
                if valid(segment):
                    segments.append(segment)  # place dot
                    if dots - 1 == 0:  # if all 3 dots are placed
                        update_output(curr_pos)  # add the solution to output
                    else:
                        backtrack(curr_pos, dots - 1)  # continue to place dots
                    segments.pop()  # remove the last placed dot
        
        n = len(s)
        output, segments = [], []
        backtrack() 
        return output
        
        """
        res = []
        n = len(s)

        def backtrack(i, tmp, flag):
            if i == n and flag == 0:
                res.append(tmp[:-1])
                return
            if flag < 0:
                return
            for j in range(i, i + 3):
                if j < n:
                    if i == j and s[j] == "0":
                        backtrack(j + 1, tmp + s[j] + ".", flag - 1)
                        break  #in order to avoid segments like "0**"/"0*"
                    if 0 < int(s[i:j + 1]) <= 255:
                        backtrack(j + 1, tmp + s[i:j + 1] + ".", flag - 1)

        backtrack(0, "", 4)
        return res
