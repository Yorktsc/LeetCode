# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        #pass one
        curr = 0
        for i in range(1, n):
            if knows(curr, i):
                curr = i
        for i in range(n):
            if i != curr and (not knows(i, curr) or knows(curr, i)):
                return -1
        return curr
