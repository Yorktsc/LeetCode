class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        """
        cands = [A[0], B[0]]
        for i in range(1, len(A)):
            a,b = A[i], B[i]
            if a not in cands and b not in cands:
                return -1
            elif a != cands[0] and b != cands[0]:
                cands[0] = cands[1]
            elif a != cands[1] and b != cands[1]:
                cands[1] = cands[0]
        cand = cands[0]
        first, second = 0, 0 
        for i in range(len(A)):
            a,b = A[i], B[i]
            if a == cand:
                first += 1
            if b == cand:
                second += 1
        return len(A) - max(first, second)
        """
        
        def checkPossible(A, B, val):
            for x in xrange(len(A)):
                if A[x] != val and B[x] != val:
                    return False
            return True
            
        for x in [A[0], B[0]]:
            if checkPossible(A, B, x):
                countA = len(A) - A.count(x)
                countB = len(B) - B.count(x)
                return min(countA, countB)
        return -1
