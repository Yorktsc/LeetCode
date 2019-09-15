from collections import Counter
#from collections import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        ct = Counter(words)
        ret = []
        for key,val in ct.items():
            heapq.heappush(ret, (-val,key))
        return [heapq.heappop(ret)[1] for _ in range(k)]
