class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        #Approach1, beats 28%
        """
        intervals_sorted = sorted(intervals, key = lambda tup:tup[0])
        print(intervals_sorted)
        for i in range(len(intervals_sorted)-1):
            low1, high1 = intervals_sorted[i]
            low2, high2 = intervals_sorted[i+1]
            if low1<=low2 and high2<=high1:
                intervals_sorted[i+1] = [low1, high1]
                intervals_sorted[i] = None
            elif low2<=low1 and high1<=high2:
                intervals_sorted[i+1] = [low2, high2]
                intervals_sorted[i] = None
            elif low2 <= high1:
                intervals_sorted[i+1] = [low1, high2]
                intervals_sorted[i] = None
        return [tup for tup in intervals_sorted if tup is not None]
        """ 
        
        #Approach2, beats 18%
        if not intervals: return []
        intervals.sort(key=lambda x:x[0])
        res, curr_start, curr_end = [], intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            if curr_end >= intervals[i][0]:
                curr_end = max(curr_end, intervals[i][1])
            else:
                res.append([curr_start, curr_end])
                curr_start, curr_end = intervals[i]
        res.append([curr_start, curr_end])
        return res     
